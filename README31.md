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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ddbfbb7-45f6-39fc-8e8b-01ee204d4461 | -11.52891 | -49.62698 | 2026-09-07 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d0970fd-b99f-39e8-94b6-3c44effe8502 | -5.36588 | -56.02047 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61bad1f5-011f-3575-a5f3-fd342fd55413 | -3.62667 | -54.60719 | 2026-09-07 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ddaa0ea-74c8-31ea-b301-498d18aba189 | -5.36462 | -56.02856 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a8ee61d-0937-33a9-908d-6d6c26f6d783 | -5.5723 | -60.15973 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed891d19-cbaa-3eb0-9cf3-31bfcc5c7c77 | -3.76627 | -61.75844 | 2026-09-07 05:23:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 336ad982-71b7-3df6-8cb2-d7fa4dda8614 | -2.55996 | -59.4438 | 2026-09-07 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ce0b9e9-8b64-3872-bed4-47eac859b293 | -3.38766 | -59.41212 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f0b8e21-d06d-3354-9e2d-ffed37ddaba4 | -8.72752 | -62.43506 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd8d3500-1c5c-3109-842f-5f7b17a30b79 | -5.48603 | -60.20425 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90b49f9c-8129-396a-bbc3-3815356fb7c1 | -5.45721 | -60.17759 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb2ae451-5be7-37c5-80c3-32e071fe7b38 | -5.36629 | -56.04123 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19e93d88-7f36-3330-b420-ff6b6ec61c57 | -4.12397 | -56.34622 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65fa8edc-e89a-3cda-9630-4e05bce4dbf9 | -4.03756 | -52.07139 | 2026-09-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60a13658-f305-34bd-9c69-be5088b30041 | -5.8315 | -60.25518 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 905e997c-1676-3024-acaf-d25370bddfa4 | -5.98951 | -57.7066 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| abdddf94-b258-33f4-956b-6ec2808916bc | -8.70277 | -62.43096 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52085965-8367-3479-a11d-1f29056bcd05 | -4.3444 | -56.28048 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48d3190e-bd1c-3734-93ed-b71e402c00ce | -4.2112 | -48.56365 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c323387-e7c5-3fc4-bd4a-f561faec7f75 | -1.62023 | -55.16587 | 2026-09-07 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb9d3f87-737e-3d85-be77-216133043113 | -5.35938 | -56.01534 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9213e7da-3ed4-308a-99bb-211fb640b063 | -6.13827 | -57.71505 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8802c38b-dae1-37c4-b14e-024272f562ca | -3.78183 | -58.85574 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 002883c5-ac4e-3683-ae63-90c8a063c3f8 | -2.73545 | -58.18949 | 2026-09-07 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e9a3761-06d6-3a53-bf52-38bc9675791b | -4.10797 | -49.06475 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68fb3880-b5d0-3d33-95c4-a100695eecfa | -3.55018 | -48.18271 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1119e768-ffbd-3034-a373-0f3258ca14ba | -5.29928 | -60.14161 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9fc95b6-dd84-304d-bde7-19c7929c5b40 | -5.64742 | -60.24027 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8221af91-dc90-3ca9-8193-6ba249e22f00 | -4.43442 | -55.10099 | 2026-09-07 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e1e007b-9d37-3b93-9ad0-9b752aa57c9f | -6.12591 | -57.70579 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1d1472c-6f98-3e51-97f7-e8a97e80651e | -3.13883 | -60.66278 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3625d74b-01ec-30ec-90b5-69e7cb3110f4 | -8.75292 | -62.43518 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08d63e08-bea2-34bd-a50b-a380e6aa8488 | -5.41251 | -60.15591 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b2dbb73-af6a-3d5f-8686-bebbc360bd8b | -3.15983 | -50.82467 | 2026-09-07 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f330a398-961b-39a9-8b79-19902aacab5d | -2.82411 | -49.23222 | 2026-09-07 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5efa50f1-f869-3a83-b656-70712400e8a4 | -3.24783 | -47.24792 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bed30c4-7326-3279-9e6b-d0bd33ccfa9b | -3.95676 | -59.35917 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 391f26c4-eace-340d-b0a3-95d2826f479e | -4.28986 | -59.95631 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dd1607f-0692-352e-a6bf-60e8bf28d373 | -4.35199 | -48.97725 | 2026-09-07 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82f35e9a-aca6-3c7f-8757-321fd6a9d019 | -2.63621 | -46.77543 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 36b73a8c-e699-3b2d-b1f9-56907146c75a | -8.75975 | -62.4158 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 797d6012-c536-3417-9dd2-0e01bada94d4 | -8.76064 | -62.4324 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a652bbbe-3179-3533-a9b4-09d8c8fcd252 | -4.21905 | -48.5648 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c49eab9-0d1c-3336-8be4-d4a090ce96ee | -4.67186 | -55.63309 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1378e8a4-c04d-39a2-b7c5-d713d3815f9f | -4.21281 | -48.56774 | 2026-09-07 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c727ba84-c362-3cc0-a664-ec9c272aab5d | -6.44043 | -58.15169 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed660879-1c45-324d-81de-f569681133d0 | -3.14718 | -60.63302 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c785499f-049e-36ec-ba1e-cfc5dc30f676 | -4.1205 | -56.34569 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 754d31c8-9f39-358a-bc91-30b6aea951e1 | -3.13781 | -60.64709 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 440b3535-c6e1-3a33-bf8f-5214ed3f9ea8 | -8.75711 | -62.43179 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 039194f2-f9ff-3edf-817f-41f97c58de5d | -2.97726 | -54.01979 | 2026-09-07 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22df2f2c-aeae-3d85-92e6-80892014770c | -2.84356 | -59.2654 | 2026-09-07 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1be51216-2cf6-36ea-a9c9-0b417e19385b | -4.97924 | -50.63347 | 2026-09-07 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a4cc610-504b-30c1-a325-3c091f83328a | -3.44364 | -59.25278 | 2026-09-07 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0efb4f80-b9da-342e-b05c-460c96ed93e1 | -8.54271 | -63.88116 | 2026-09-07 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98fa82fe-e8ec-3321-8555-5fdb17ab19ac | -5.44281 | -60.11704 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7723f1bc-5a34-3531-b5a7-0a765ca17c75 | -3.34001 | -53.40543 | 2026-09-07 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef509c47-1f8c-3251-9331-6f634bf90f98 | -6.51002 | -58.29213 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99ec7e9e-80e1-384f-8bc4-ad09c805755b | -5.63577 | -60.20554 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75969985-cd5d-3431-97a5-9eb076a02a0d | -2.63067 | -46.76978 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 9d76032c-b361-3bdc-94e7-d5bb64748898 | -3.14168 | -60.66711 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8cb5e9b7-8d34-381d-827b-8586c101d184 | -6.50669 | -58.2916 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 977c2fe0-2d74-37b0-a786-892996abca5d | -4.2205 | -59.55799 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a191e05f-f848-3c06-b291-90388258dcc2 | -6.44155 | -58.16634 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a322858-c859-380f-854b-938c9018f3e8 | -8.75556 | -62.41919 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d40ce01-a329-374a-a65a-0eee82c46c2e | -5.15358 | -55.96653 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8421f84-5574-3dc8-b3e2-3c37a8dcf741 | -3.09074 | -61.07167 | 2026-09-07 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2111f82-19df-32e5-9ab3-0caae1c3c0a9 | -5.99344 | -57.70351 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c0bad2fb-462f-39e1-b954-90cc29e05096 | -5.98726 | -57.69891 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85a0449c-e40a-3dcd-8ee3-0a67e4596f9e | -5.99792 | -57.69685 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6e0db4-43e2-324f-b0a7-3873b04d9409 | -1.20153 | -55.74064 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3ef3cfe1-3de2-3f3f-8c95-fb684a49d107 | -6.56829 | -58.97934 | 2026-09-07 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462db716-e32f-3b0e-9728-5012ac3e3b07 | -2.95616 | -48.70346 | 2026-09-07 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a649fb72-1156-3397-ac5f-77c7dd0b5464 | -5.28479 | -60.1247 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6feaec75-a642-3735-994a-be6eb46b8428 | -3.39602 | -61.31341 | 2026-09-07 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c9b16de-79cd-3799-b5f4-502b407e7336 | -8.74011 | -62.42481 | 2026-09-07 05:23:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08510278-8b93-323e-8c31-4b47a9defaf3 | -5.35455 | -56.02292 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c6094d3-a57d-33e8-8365-37c2c46bea53 | -3.38043 | -59.41457 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b31d30b-f949-37bd-b7f2-fa40c4c6ac38 | -1.20102 | -55.7212 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6d2fbe1-7724-389a-be18-d6cbdcb839db | -6.87317 | -55.6016 | 2026-09-07 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6628c661-99e3-39aa-867a-959d7f7785bd | -5.15987 | -55.9656 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1883929c-45da-36b7-a6d7-745170b6b60e | -4.50487 | -55.71608 | 2026-09-07 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b22debe-9b1b-3ecd-8159-70bc38da1196 | -2.9779 | -60.94175 | 2026-09-07 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa849b1a-c462-39cc-879d-c723dafeba28 | -6.13151 | -57.69193 | 2026-09-07 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ed52d06-5c02-3483-ba98-ebfbed9ae343 | -1.19696 | -55.72446 | 2026-09-07 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da5db0bf-4c86-38ff-ae93-6343d45b9eca | -5.14226 | -55.96892 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fed11a74-690b-3f79-b78f-8cedabf5061d | -5.30099 | -60.13094 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eda269b6-3562-3036-9ed2-4e7b21ac2b1d | -3.5496 | -48.18667 | 2026-09-07 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48e2a240-9aeb-3e4b-afaf-99cef714db5b | -3.38321 | -59.41859 | 2026-09-07 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2264ceb8-2e6d-3bb0-b75c-3ef9522e5815 | -5.30542 | -60.14624 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e29b7d5c-b9fe-318a-8008-374d282b75c0 | -5.36692 | -56.03719 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc37395a-c570-31b8-a9c5-7fd7f8bfe8fa | -5.3679 | -56.02373 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31f2dc45-37a4-3049-a7df-e1342345377b | -5.274 | -59.96293 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a482d628-e7bf-393c-8de5-82b29b07933e | -5.48661 | -60.20069 | 2026-09-07 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cba115c4-0a16-3408-9395-8bb4ea4be024 | -3.77907 | -58.85177 | 2026-09-07 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aa12edd-7261-3237-aa75-64e9c629a7af | -5.36546 | -56.03994 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 342efde0-f179-3947-a882-5d6b7ab46453 | -4.12196 | -56.34945 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbd297af-6c8c-3963-a9cf-f733a935b688 | -4.40859 | -60.07764 | 2026-09-07 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a9e127-b9a3-38be-b4d9-44349489ce0d | -3.7501 | -55.96667 | 2026-09-07 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ab7e336-b77a-3250-a922-085e5be615e6 | -5.35812 | -56.02346 | 2026-09-07 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
