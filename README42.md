# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28704c3d-412e-3e03-8fc8-d0803018d455 | -7.58803 | -49.18844 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e18fc71a-548d-389e-addc-44e77be59614 | -7.58751 | -49.17014 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0297008b-d74c-3eba-a9f5-9d5a3312a47c | -7.58694 | -49.17369 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3d54d5f5-df3d-3b6a-bd72-2d7064ceb801 | -7.58581 | -49.18079 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da2a2e86-8d2d-36f2-8444-a49071ef85ce | -7.58525 | -49.18434 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 192bdc9d-584e-32fe-bed3-fd1f07a36b9e | -7.58468 | -49.18789 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9fb2640-bc60-3525-9a6a-973c24c52644 | -7.58359 | -49.17315 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd77bb6c-809e-3cbf-a888-cf8003ebae88 | -7.57128 | -49.18576 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb6bee8-f0d0-3f8b-b181-1a7f3f1f91fb | -7.57071 | -49.18933 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 183efac5-8adc-3bd0-bc9d-1fd4a7773179 | -7.56949 | -49.41343 | 2024-09-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f172d8-b6fc-3f9e-80f0-fdeb111c6b58 | -7.56835 | -49.4206 | 2024-09-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f82086-492e-3df6-acd0-89b61abfc47a | -7.56736 | -49.1888 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07ab245b-0111-3649-8399-5e06d486f354 | -7.56663 | -49.43141 | 2024-09-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9436ec9-4593-3d1d-bfda-7430ace203af | -7.56326 | -49.43089 | 2024-09-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 638eb4c7-fe1b-3b3e-906f-7c7375c08327 | -7.27477 | -49.48548 | 2024-09-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e493ecc-2795-3ff1-a27b-3697af6056cc | -7.27139 | -49.48494 | 2024-09-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60baafce-42f1-3d44-b414-b764a52469ab | -7.75081 | -50.01394 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61674c88-2636-388c-91ca-ec9c2c4f72ba | -7.74859 | -50.00597 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b833e906-4c49-39e9-a85b-13c6d49e479f | -7.74798 | -50.00972 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40688e26-f2cb-3657-8395-028699e27320 | -7.74754 | -49.99077 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1c9dd12-ffb9-3289-b04c-63fe2da0c2e5 | -7.74737 | -50.01352 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b53cb9d6-8e66-352c-b49a-285c8b7b2d14 | -7.55972 | -49.69898 | 2024-09-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87fb1301-ac96-3617-9863-7ec064172e7f | -8.10268 | -49.963 | 2024-09-30 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ca30411-b34a-31ee-a3bc-230d894dd25b | -7.88606 | -50.00144 | 2024-09-30 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfbe6afd-0054-34f6-bebc-e2c5a0d8c95a | -9.32822 | -49.14114 | 2024-09-30 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 571af329-f1bd-37e8-86d8-c713b196642c | -9.32489 | -49.14061 | 2024-09-30 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc97f2d2-3cb8-39e4-9413-f6497526c29d | -8.61823 | -49.48166 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29d149f7-4bad-3f12-9df8-fdcd68083d1d | -8.44881 | -49.13742 | 2024-09-30 04:32:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d66e0edc-3bdb-35d6-a1a0-f4ad18905f46 | -9.05597 | -49.84079 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40fc0cb2-3730-3c7e-9794-15065a1223af | -9.0526 | -49.84024 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4fd62a5-bdfd-3e01-a2e8-3806085bd6dd | -9.04365 | -49.83131 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7347a78e-2fd2-38ab-98ad-80da95003341 | -9.04087 | -49.82713 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53b4627a-56fb-36da-b634-c9896e5e024d | -9.04028 | -49.83077 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dce5838f-f281-3aeb-9df0-34c2b0231ffb | -9.0369 | -49.83022 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fee8910c-5c0e-32c7-a047-052e7fd45889 | -9.03353 | -49.82967 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71714b83-0d71-361c-a38b-bed03d0a0455 | -9.00106 | -49.8287 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29b23e20-81a3-33a5-84f7-3d7a0934c894 | -8.99768 | -49.82814 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2929422-fa47-3a17-a482-f4dc8b5f02f6 | -8.99489 | -49.82396 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a9d2bac-eece-3918-870a-b35c4f959c8c | -8.99431 | -49.82759 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 556fbc39-8bff-39e9-85cb-a2294ba47eaa | -8.99151 | -49.82341 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1d9eba3-74f8-3e50-963f-bc407685173c | -8.99093 | -49.82705 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f14ce32b-ff58-3a85-96a2-9a844fa7b078 | -8.9673 | -49.82319 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b50f6672-06e7-3b63-aa09-6a24fe4a2b78 | -8.96671 | -49.82682 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6fd1bf3-fe34-3859-9083-0a84558351a5 | -8.96393 | -49.82264 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b07878b7-578f-36b8-9d01-13c1a2851777 | -8.96334 | -49.82627 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5dda3b7-f034-375b-9d09-37eca766a80c | -8.95996 | -49.82572 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfecf9c7-c1a1-3588-8c4f-905fdc356b5f | -8.93382 | -49.72126 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0e33751-e625-3b69-a574-1868d1785d32 | -8.93046 | -49.72071 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa002234-8afb-3b45-a6cd-307b0fa2b5fc | -8.89607 | -49.63365 | 2024-09-30 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c89ea51-82fe-328c-9994-d8caec566e41 | -9.74152 | -50.4358 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bf55eff-bd3a-3dc3-98f4-8d44c9b6cc63 | -9.7381 | -50.43521 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7616d62f-7732-3ee0-acfe-447f7b9c1c6b | -9.58384 | -50.19646 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bd2a7d8-e3e2-31d3-9970-f5c4d4f8f3fb | -9.58324 | -50.20015 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68c59b13-eceb-367e-954a-4be791170184 | -9.58265 | -50.20384 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83d10c78-5b44-3690-afca-9b485e8dfacc | -9.58205 | -50.20754 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0e190553-ec81-320e-a9a8-8fb9bc50615e | -9.58145 | -50.21124 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9a99735-a1b7-3f7f-8bb7-2972e5ece222 | -9.58104 | -50.1922 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11f3bd8a-ca9c-3d18-9398-21f67d651346 | -9.58044 | -50.19589 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c532eb1e-a23e-3a10-9ded-36e0705b128f | -9.57985 | -50.19959 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25642389-217b-3d57-967b-850c2df3ab73 | -9.57805 | -50.21067 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f37f6aff-e409-314d-acbe-c267f8a628c5 | -9.57764 | -50.19164 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06909385-413f-3d49-9fa4-6cad2ea9df28 | -9.57746 | -50.21437 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5500b6d5-ffac-3a0f-89ca-8d2b69d6ddc5 | -9.57425 | -50.19108 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 213d3053-8008-360f-b019-ab7829cebca5 | -9.57406 | -50.21381 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97ba164a-82ed-35a4-8bee-80222aebece4 | -9.57346 | -50.21751 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97484b7f-66cc-30af-83ac-28beccd21e5c | -9.57085 | -50.19051 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53f67e9a-b3a1-3ce0-a50f-1899b3523afd | -9.57065 | -50.21326 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8945160c-56e0-3901-8307-f41fa75fcf16 | -9.57006 | -50.21695 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4107c50c-f631-3f9b-834c-803ff4b5e0ee | -9.56785 | -50.20899 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9527e16d-ccc0-3f3c-8406-229d830300fe | -9.56745 | -50.18995 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0628f11b-b8e8-3aa1-b22c-acc11b220c71 | -9.56725 | -50.21269 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b801d106-ccb1-37bc-85c0-dda92cc256bf | -9.56685 | -50.19365 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e11ff02-4a2f-3b0b-849f-a3440f899d68 | -9.56465 | -50.18571 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f241089-ef98-38d2-98f0-f182290ab10c | -9.56405 | -50.1894 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 205c468f-f361-33a1-a32b-b178c2692004 | -9.55705 | -50.21101 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac89844-fc20-3779-abfa-ccc94fb9ace1 | -9.55305 | -50.21415 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd2fa4d-5a99-39a1-8970-8136c7de91b5 | -9.54965 | -50.21358 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c18cd5-3fce-36c8-8c04-61533d5b31ae | -9.54685 | -50.20932 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f3b1a16-b598-3efb-a4f4-113e746a1469 | -9.54345 | -50.20876 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b57b6939-2d42-3a89-8b91-afa44276b17b | -10.05005 | -50.30956 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06788f99-4815-3ec6-abde-eb4e8fffc7cb | -10.04725 | -50.30529 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ab3b7af-9115-3714-b737-4b4490771106 | -10.80496 | -50.12811 | 2024-09-30 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71960dd6-8564-3e04-b5c5-6003381f9996 | -9.92448 | -50.08615 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e31fa43-6382-39a1-ad45-2db899399106 | -9.89685 | -50.08535 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ecf7d10-6e0e-3fb0-b6e8-87686a8dc8a7 | -9.75325 | -50.10682 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64d20b46-7633-3229-90fe-7291616c94b8 | -9.6794 | -50.10635 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82da0a25-5071-3a37-8ab2-2e4a3facf912 | -9.67661 | -50.10212 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12b4270b-d8b5-3556-aef1-d3f0f3159062 | -9.67601 | -50.10579 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb6dc4f8-cd58-32b1-8a83-20f4e5fa7a4a | -9.62757 | -50.09787 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e00381d5-9d1f-34c0-9eb5-d1193c84ca04 | -9.6236 | -50.10098 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea4127b9-1016-30dd-b5e1-e7a51401e7ca | -9.60666 | -50.09818 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5c44b4e-3747-31e6-90cd-4b674013091d | -9.60327 | -50.09763 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 671e6814-df6a-33fd-bba3-70155a47e2af | -9.59548 | -50.08128 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 973c2ab6-2d30-3087-a1d0-7187631ad9f9 | -9.59488 | -50.08495 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 555701a3-e19f-3c75-a1db-297a81e07ab5 | -9.59268 | -50.07706 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b3592f6-ebf1-34c6-b7db-b1ebe5ba0ee1 | -9.59209 | -50.08072 | 2024-09-30 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362c4780-c0a8-3fce-bc49-6f008ede827d | -9.58217 | -50.12054 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e41d9788-2abf-3071-bd90-1293eeb15a5d | -9.58158 | -50.12422 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a4bfc25-cc8a-375f-9d92-9e532822554b | -9.57878 | -50.11999 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d976c349-ad15-3bcb-84e0-bafaabad8bae | -9.57819 | -50.12366 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README43.md)
