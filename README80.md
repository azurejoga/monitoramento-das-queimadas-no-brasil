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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd9299cc-9b90-3057-9b24-adf59ddf41b5 | -1.18938 | -54.17629 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6058c74-d1df-3aba-b053-df76499c5332 | -5.70018 | -41.72833 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f34844fa-30fa-3af6-90ff-3beec684bbea | -2.73898 | -54.13047 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd595574-3045-3914-aa1b-a37e26e9ceea | -3.25235 | -50.39879 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e00a06b-0b96-35ed-9143-3fcdee9dedc2 | -3.53019 | -54.6651 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbfdc83d-5b8e-30e6-bbf6-7c30804e2baa | -2.98444 | -54.07737 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d370f548-83a7-37a6-829b-cb0200872c66 | -3.89874 | -58.96286 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6518e16-98c2-3ae7-bcf3-ed36601bcd7b | -5.09398 | -46.22157 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f15ce7b3-e951-3fd7-bedc-2a40a6553d95 | -6.1431 | -47.92354 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e440924-ca4b-301b-8997-d5f764c530ba | -3.20361 | -50.55139 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e513f8d2-7a83-3d4d-ba99-2fbe13ef5296 | -2.13863 | -54.47013 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c3e3591-3f3f-3ea1-a5ac-fe63da5241d9 | -3.02441 | -54.08046 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2162a812-b3d9-399a-a51b-1bb16d61d01f | -5.88438 | -43.45877 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5647cbdc-edd5-36cf-a511-07b5481ce14c | -3.77904 | -58.58973 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7c993bed-e1b8-305c-8607-ec8b1247efda | -4.98257 | -46.04245 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 303316e4-733d-386b-b114-8f8e300bd442 | -5.83804 | -43.80886 | 2026-10-09 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df5fb8ea-7d83-3482-aff4-0df6d045c3dd | -3.1648 | -50.58991 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 220d0eae-b50e-33c1-a712-d58f1b16e1e7 | -5.71051 | -53.46344 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20505fac-5f13-3c08-be0b-abe4f683c31e | -4.29283 | -48.60212 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9169bad-9dea-3527-8863-f160bb78d827 | -3.67744 | -55.94912 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20a1171c-3b4e-3bb2-aca5-13396c7a03ab | -4.09207 | -45.9021 | 2026-10-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 802e50ac-6e59-3e27-bb68-e1775be5ac7d | -5.70518 | -53.45997 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f1d243e-8c1b-336e-95a5-8de6d8f76c63 | -2.23594 | -51.92421 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3081484b-d86b-3fc3-a395-89764c24fd01 | -5.41484 | -44.6277 | 2026-10-09 04:25:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a770a32b-df13-3c4e-8ce3-1a5f8e030fe5 | -2.99117 | -53.84789 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38ced9a3-5559-3482-8251-525d979198b4 | -5.71839 | -41.76659 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e089217-56f4-33b8-9db4-94ac6719bfcf | -1.53755 | -54.54993 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b89e96e2-585a-37a8-821a-43d58c7cc3cf | -5.68489 | -49.04419 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c40c7aa-0c7b-32f5-9baa-6de35fc1f6c1 | -6.16403 | -39.44164 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 09afec60-ce1a-356d-867b-9a39e7b98662 | -3.00192 | -53.90705 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02fb0370-58ad-35c2-a9eb-acfb06dcf353 | -3.58723 | -54.57745 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f854e0c8-27dc-3fa5-8203-0308b133f29b | -4.64255 | -50.95896 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d16a007-f7a5-3840-a8dc-d3e1228dd738 | -3.29421 | -54.00665 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b483b22-0790-3e72-a1c3-36b2f7b0c39e | -3.01787 | -54.08849 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ff29e79-c15e-331b-81e4-81b51105f890 | -3.00825 | -54.08397 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58b98093-8493-3e94-82b7-20a61f91085d | -3.16877 | -50.59054 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 763e22fe-897b-39e3-a1ea-3a5ab7607a5b | -5.17233 | -45.60958 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b67926c2-9b01-3356-b119-54561fdf18c9 | -2.93806 | -53.9194 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a34c2f32-a9a8-3629-a178-8110d2d6a99b | 1.05712 | -50.03527 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fa0d211-163b-3630-b9ac-4352f722bc55 | -2.92501 | -54.12256 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 093d0fa6-820d-3506-98d6-443d4a31db93 | -3.26857 | -54.06801 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc9fa89c-b34a-38d5-9966-5f6c8bd8725c | -1.48014 | -55.86958 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04f12b57-9c82-30b2-9819-e6476a6963aa | -5.39647 | -45.65554 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 427949fc-bc2f-3c29-9983-5c0e968ec881 | -3.17093 | -48.6979 | 2026-10-09 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84e4b42-ceb7-383b-98a0-5faad62a9f8f | -3.17386 | -50.58431 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c304fa1-18fb-390e-b296-19c2bc5f72c7 | -1.62959 | -55.1252 | 2026-10-09 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74cf7bb1-287e-3469-b82c-e306ab21e54c | -3.54625 | -54.63259 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5642f3f-d938-3fc0-8beb-978e4f2c3547 | -3.27555 | -54.05707 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cfa1ce4-415c-3a9f-ab02-fe44d77241c0 | -4.7367 | -55.66307 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4e070444-b628-3740-ba0b-395a1e71f277 | -3.93169 | -56.02849 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d70cc12-bb18-3970-b38c-0c8007649378 | -4.56231 | -54.21136 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff7088e-4155-3146-b7ca-f058de0d35dc | -3.43655 | -54.54623 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c245bc87-a12c-3dae-907f-4c2513fc7871 | -4.50783 | -45.81261 | 2026-10-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c44c7644-5062-3b8d-b2c7-bdea8722ec09 | -3.72986 | -53.6964 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ebd23b17-24e7-3e6c-8a5d-bd8433a28b5a | -3.03709 | -54.09768 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ae1469-b1d9-3ecc-8e59-df2dd9418a8f | -4.27989 | -49.08857 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0126941f-53fc-3cc2-8f63-e6df35257a3b | -2.97553 | -54.03677 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759936a2-1770-3931-a2e0-d4e106cd8d03 | -6.9603 | -45.2829 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d0cd0e70-8d80-334b-ae8b-801e751c49d5 | -6.43059 | -45.94141 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33bacc20-92f0-3f90-b0a9-ae258ddf333c | -3.30495 | -53.69827 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a91b24ae-38e6-3dba-b5cf-c40f7d97e4fe | -6.513 | -45.4071 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5446f18b-d02f-3f1b-a865-7b09f553c8b4 | -4.63744 | -50.96518 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 011ff0fe-8160-35ae-8c12-42c7f4d1ff60 | -2.37543 | -48.22466 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7376f093-4151-3ff9-9a38-2c9d4fc39056 | -5.3822 | -45.94313 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae3d92a-ad9a-393e-a7d1-2af20d5ed54a | -5.26563 | -50.14326 | 2026-10-09 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa34ba01-51a9-3149-8bdf-6b8356fccd5a | -2.90321 | -57.21987 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9eb626b-c4d7-36d9-b3b8-f7023d854b5b | -5.10663 | -46.22704 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2f986a8-7d48-3bb6-9718-083a023e7e84 | -3.01936 | -54.07964 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70524071-c13a-360c-9520-d7268434ebe4 | -6.22087 | -44.14858 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3784ed57-efab-34da-b299-3d5622107df1 | -7.02515 | -45.30731 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97d7f54-34dd-3cd6-ab3c-cc4b907527cb | -3.52804 | -59.5741 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9ad70157-44e6-302a-8617-ae24861d1e9d | -3.25379 | -54.03304 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c200adb6-f3fd-35d8-afc9-de7642c13766 | -3.56662 | -54.67146 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6628e7b2-4508-3c65-82f7-67ac6c9337e3 | -3.01581 | -51.01598 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05ca9b35-0c3c-307e-9e97-3e84738fefe9 | -5.98689 | -41.36929 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b5f8ff7-7583-34de-8898-22aa2c1f81b7 | -6.87788 | -45.90807 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3bd7d75f-9e70-37a5-b5a2-833ce458d1a4 | -3.27353 | -50.3919 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86b420c6-5f25-32de-a476-102f6ea60e60 | -3.34695 | -50.41165 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73de9d31-53ea-3231-9e21-c3c5b0be6c31 | -3.00609 | -54.07172 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc2ef6b8-027d-37a2-8bff-8062c65f160e | -3.25706 | -50.39445 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 756dac38-3f54-3258-836e-4d951c425465 | -3.35399 | -50.41784 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a07f5cdf-08e2-30db-b9aa-408c0e98b5bf | -3.5693 | -54.68792 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a968bd22-7b68-387a-a465-ae4683715676 | -4.40413 | -43.11703 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07920a95-5217-35d5-9f30-696819955125 | -3.02688 | -54.06576 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e69a4f2-a54a-382c-a363-3c35aa116d47 | -5.95525 | -40.93026 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ac932bc-9c9f-37d9-812a-507ec43e81dd | -3.10616 | -53.92949 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea5d5b36-d345-35b0-830f-f3b6c0bd0117 | -4.32872 | -55.02096 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfd2330b-7ab8-3140-8890-c932f8ada391 | -3.3128 | -53.71148 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c400c09-be5c-395f-97e1-40fcc6e3cafe | -5.74696 | -45.34615 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca39b0a2-6593-38b4-86b8-322b04945ba6 | -3.17259 | -50.44584 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20c46f18-9c50-33eb-8ca7-0e6cfcab3a42 | -5.69283 | -53.45526 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8efa76b-ca58-3d4d-9975-87bda0e44f5f | -2.7601 | -54.09703 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77d4582e-2f48-3834-9394-01483dc521b1 | -3.1597 | -50.59615 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a81dc962-2122-31fd-a5a9-ca9c7de0d978 | 1.11886 | -52.50182 | 2026-10-09 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2043d291-9744-3e2d-a30a-1f738e076e6a | -3.52666 | -49.26566 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 671943d8-e010-3b30-8749-370fcfb7b5a7 | -3.54107 | -54.63161 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a7f7044-ef7c-3ef6-affe-0c6108c869a1 | -3.36565 | -50.47095 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20f02250-ed07-3df9-994e-5beb1b609f02 | -3.53123 | -54.6588 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e5b093f-9798-3dc0-b721-6bfa73a106cd | -3.11073 | -53.77771 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 318c2dde-7feb-329c-91f3-6a9fb3edee9a | -3.50334 | -59.26488 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README81.md)
