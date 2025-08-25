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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3a339e8-a245-314c-8913-04a8f0e7479f | -6.79649 | -58.63854 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b743f577-4a0d-3ec0-8686-c1ccedcfd68c | -8.98276 | -65.41078 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 13f72232-5941-381c-866c-b70fcc291a8c | -7.53231 | -63.81202 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2975b2b7-41d0-32a7-9b61-b4c9b5c5329b | -8.05649 | -49.67506 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2be35c4d-f6c2-3226-a6ac-cd168af851b7 | -10.70601 | -50.55544 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f687c69e-a552-3309-a822-60697d152a1e | -9.16067 | -59.46737 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2705830-5fb2-3652-a386-ee9280e78f50 | -9.15133 | -59.45738 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ce2b7f-d8d6-3242-8bef-e0def6ad32cc | -6.4932 | -49.90993 | 2025-08-25 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d352e760-a061-3909-bd33-cee765415ade | -9.20588 | -60.91622 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf810185-469d-3d47-a6b8-8d0a8c03b5b0 | -8.97695 | -65.41302 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7fa0c545-f16e-3471-b926-e4e876915845 | -8.8904 | -62.44106 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b26c5413-8e39-3eeb-9ba9-921678c90842 | -8.65597 | -63.42862 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc254340-2e96-3ac7-b257-b8bacfe12d8e | -12.29696 | -49.14225 | 2025-08-25 05:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1ce6d02f-24fc-30fe-afbf-b80e53e50d8a | -8.22506 | -61.38294 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f52e9c48-b748-3a76-a767-f2fe3fc1dbb5 | -7.59129 | -45.24583 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 006e7759-bd61-383a-a27c-c6b43e9c8dce | -8.97615 | -63.11111 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b162fe6c-0339-3178-a1fb-4f6c6c7eab3c | -11.63948 | -46.21996 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4fb19c6-3086-3090-a5f5-e50affb3535c | -9.19062 | -59.6427 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19cba273-95fe-3ce2-8719-8d9c35be06a0 | -10.25643 | -59.10941 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c335d0b8-dd54-3c6a-8182-4b7b87453f26 | -11.6389 | -46.22471 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 649333d6-6859-31e2-9e19-d722831ed3fe | -6.82421 | -58.95265 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8bdeb831-7b86-3614-919f-6cc6a1f32545 | -7.17706 | -45.1628 | 2025-08-25 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3225ce9-e952-3f73-8dd2-94189d96c654 | -6.68918 | -58.85327 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34af77ea-80a0-36c8-9943-18a0ce6df330 | -10.71467 | -47.13642 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1679395c-ee07-3b18-a169-06bdbb6c194e | -9.21745 | -60.91116 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ebf1c09-e9b1-381b-8897-938b485380ee | -6.90221 | -47.93105 | 2025-08-25 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97cc25f8-4700-3680-9af8-3b83b10b9388 | -8.12069 | -62.86963 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07a97df2-50a1-3ff3-bac8-725514c4fb1e | -6.90271 | -44.41317 | 2025-08-25 05:04:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5923df73-e05c-31d7-afff-290968e7e2ef | -7.66556 | -45.39627 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ffcdf3b-aa54-3f9c-8e45-11cf0013fd07 | -9.12837 | -60.73636 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14f415b7-81a4-3e88-b67c-fb43e9f983b6 | -8.22485 | -61.40881 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3659ea51-3923-36f8-b20c-c8bc35d34052 | -8.88612 | -62.44029 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e76e3f8c-7362-3bf1-ad90-36e84eba1318 | -4.96006 | -55.8205 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8059c2ef-bf44-37c6-98f2-d52586717723 | -8.87969 | -62.42657 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6db48004-a548-3260-b918-b4f0635c72b7 | -8.07724 | -61.53972 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 865753e5-745c-3c08-93d0-02b703d3b44a | -8.06862 | -49.68605 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90d6310b-48ae-33ed-9682-13b3e9e712f7 | -10.77259 | -47.07727 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8d968a0-1431-3cfa-8db5-23c5b8017787 | -11.46817 | -55.47071 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9268615-da9b-3488-898d-ab03dd1aeb80 | -7.44266 | -57.61955 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e65ebc8-ebda-3a47-aa8c-ececbbf1c1ba | -11.17069 | -55.03415 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51979ec4-3520-3ad3-a246-37e93005c8a3 | -6.34034 | -58.19137 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb4056cb-9067-33a8-96e0-7c67fd48e875 | -6.13233 | -57.7433 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 019cf336-6c0a-3088-9b0c-36cacec72ffa | -12.93903 | -46.31919 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a111a47-d3d4-3aa3-af46-26d0f4711708 | -8.87327 | -62.43801 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1422513-90de-3d9a-b70e-0bb03795aed2 | -9.15779 | -59.46267 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12f246ab-fa48-3879-a93a-98708161b0d2 | -10.00123 | -59.95525 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56620e53-381a-39e8-b998-be1858591656 | -9.26851 | -59.78401 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a62cb526-6df5-3ccc-86f0-e715b98ae0d6 | -9.54697 | -48.14213 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 848c3f67-a3e4-31ac-b638-1061fc4dccae | -9.15847 | -59.45857 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7544b0a-9c36-3e95-b57c-2df50ab36db9 | -6.16322 | -52.12963 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 069abe97-d55a-3f55-8524-77d08fdde117 | -6.91179 | -63.00182 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f2cbe41-081c-3f4a-a0aa-a7600af49dbf | -9.16027 | -59.51387 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90245a06-78ae-3765-858e-009e5c6ee5a7 | -10.83712 | -46.41553 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 453268d9-eabd-3b1a-bd02-3fa0b7a10690 | -8.88684 | -62.46144 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d02e6c3-ba59-3e15-98b3-76c85339bde7 | -9.16698 | -59.45157 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c4056d74-fd42-3dd9-acc4-a5e01b951dfd | -5.75116 | -51.69938 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0368679d-4006-3ca8-93ef-4b50bf94a5e3 | -8.67482 | -62.87059 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42cdaae8-ea19-3bb1-93ae-d2c8f526a742 | -9.2125 | -59.44248 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25bd5927-257a-3293-8540-2d50193a08e8 | -9.00197 | -65.39442 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8109f02b-95aa-310e-a995-4acef22602ab | -6.82489 | -58.94855 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f0b5bfa8-9e95-3b7c-a1c1-05558134e5a3 | -9.81972 | -64.2592 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68f92de8-333d-33e8-bc85-97cf14d2381d | -9.03865 | -65.72099 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e65dd9f-4961-388b-9ffa-72cd56b03f23 | -10.41897 | -60.30254 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 82c84c6f-e2da-311f-b028-ae19101da9f9 | -5.42775 | -60.17087 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c063f490-e2d5-3dd7-bfc6-a43acfa68e7e | -8.21172 | -61.38801 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| da659900-ac9a-3a1f-98e4-e27a26b596ff | -9.09303 | -65.72458 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a48d571b-7545-3a04-bf45-c21a0a47b91e | -9.16723 | -60.83224 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5a61f83-9131-3111-bbd4-9bfb81487abc | -9.6511 | -59.63246 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1546ed2e-21b7-33a3-8638-47a5a3f1a35a | -10.71491 | -48.32655 | 2025-08-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21aeeb57-bb4e-3718-bb98-54e7dd06c3b7 | -10.10609 | -57.76861 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b32d1df-4ab4-3482-a8b1-a6ba5175386e | -7.66206 | -42.665 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fcf99775-f669-39c1-a57c-4cedf0d7f8a9 | -10.60547 | -54.88514 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e70ed68-32d1-3f27-9eb8-e46590e18512 | -5.7483 | -57.58036 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc07279c-3e64-333c-b971-1f24415b5e6e | -7.57812 | -45.23146 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 220e70ae-4533-3974-a2e3-6a2b11a962d3 | -13.05608 | -46.32597 | 2025-08-25 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ceb3503-e245-32d5-8274-fcd5fa7a3520 | -9.17514 | -60.80896 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06a5f7ab-b657-3a9d-b0e3-9886a986de23 | -10.0994 | -57.76751 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7499fb23-4331-3732-8683-5c8fb250a976 | -10.53597 | -57.9707 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e23fbcf0-7cce-35fb-aa24-9fc8902bd69c | -5.79393 | -59.22137 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd272cb2-00b1-310f-8b19-8b0fa1ad4b68 | -8.12642 | -62.87834 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97a6ddcc-48e9-3635-9c01-1fdc703457bc | -11.63135 | -46.23746 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a9f343-f825-3052-8cfc-70aad5b04b2b | -10.40671 | -64.39104 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3bc6c89f-8b99-33f5-8eab-027a762a8714 | -9.20286 | -59.47874 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28627084-1a58-38e0-839e-79e7b436f6c9 | -8.22424 | -61.41238 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28cbbf57-5085-3eb5-abb6-06c7acf1b3d4 | -9.5045 | -56.10011 | 2025-08-25 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84e4d62e-fe0c-31fa-b9f4-ffd6a2734a42 | -8.60271 | -62.58942 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba7cc403-1152-314a-8a02-bc785e6ae0bc | -6.81399 | -58.9568 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2cee8435-432e-360a-b1ce-8090a2329a30 | -7.90473 | -63.06361 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de6675d0-e77a-3d1b-9ca2-cf2ae3372e81 | -9.0871 | -65.72697 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 987b5c75-0cca-3295-824c-421cc559f71f | -6.82247 | -58.94979 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 095663e7-1454-3562-b203-c904a85d1e60 | -6.1966 | -44.14331 | 2025-08-25 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e6a4fb3-8993-35a3-acc2-952ccae10c1d | -9.00659 | -65.39861 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77917dd5-d91b-3435-a6f4-d94b1850f05d | -11.62551 | -46.23608 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a415cf5-3f8a-3b07-8568-6ca3c83edd0d | -9.09366 | -65.72114 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae14fe43-46ac-35ab-a741-e6127328a38d | -9.21197 | -60.92023 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d1e8b6d-415a-37d0-ba52-e0b37e324799 | -8.87684 | -62.44284 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99250d7e-3f25-39ec-850a-5f47b220e7d2 | -9.95963 | -60.18291 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 698df197-6833-302d-b539-484988a38e90 | -10.71552 | -47.12921 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e01d9c47-3997-32f2-800e-d8434d609a3a | -9.19197 | -59.45576 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5e0c580-16bb-3fbf-a4ee-e630c6c75e76 | -9.56939 | -55.37177 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README60.md)
