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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a375c8e-d235-34a8-b544-5b7d10b03c14 | -2.88964 | -54.077 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2650cee-2f74-3b74-88ec-8e7a7f993eb7 | -6.44359 | -55.05351 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64b4ece8-bf28-3949-98b0-5def3389044a | -0.91848 | -52.43837 | 2026-10-10 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 26fbb91a-4548-35c5-8441-c1b28b6974d8 | -3.87577 | -55.9859 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fd94d56-6e3d-3a6c-85cb-6700808fc716 | -2.57105 | -57.41422 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d6c581ee-bce6-33d7-8369-1810b76006a9 | -2.05899 | -61.13753 | 2026-10-10 05:48:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 481ddbfa-1adc-325f-84aa-2d8c30a055fd | -2.98869 | -53.90451 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f491b82-c732-3c25-85e6-4849bac68f69 | -6.43792 | -55.04704 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1f51c91-f15f-31ea-8267-d6d913112469 | -3.25929 | -54.18523 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7ebffcf1-7694-35e8-8b36-691d46774ff3 | -4.12198 | -59.89268 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cb6bbb2-8a7d-3c78-a4ec-246aa16fb4de | -1.87985 | -56.30593 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8b9da8-c709-317e-9c19-563c3a7bc223 | -3.31191 | -54.67795 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 957e0064-267c-3f39-92ad-de42a51f62fa | -2.83954 | -54.81311 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9901afe6-fac2-3b45-88aa-1b284e9fd5e1 | -3.3169 | -53.84068 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c541a5b-a8c1-37c7-8fbc-51626964552d | -5.30291 | -60.20633 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d60e95-304d-31ac-95af-8a4c2f8af87f | -3.0357 | -53.89399 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9c5c4953-27ad-3496-978f-835e7c1f828b | -4.58914 | -55.72866 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b78304db-b191-33de-b2bb-4ae51ad518a8 | -3.77964 | -59.19761 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 488a623e-80ea-3015-abe9-654b021a8bf8 | -6.12299 | -55.69763 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abdf8778-12fb-3436-847a-793946de9f93 | -1.62416 | -54.42483 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0d80385-e659-383b-b89f-9c405d25e0a1 | -1.62658 | -54.43616 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff1550fa-48d4-300a-ba1b-4854bd638384 | -6.12233 | -55.70236 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dcc4e645-e4c4-3f28-ad5f-9e02ab6e6ad1 | -2.34863 | -57.99108 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 415bf6e7-64f1-3bea-8606-0e70a47285b1 | -6.4935 | -55.32192 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08cabaf1-0f3a-3306-9043-9f4cfe1ff540 | -6.43975 | -55.04195 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b71942d3-e80f-34c8-8d44-85dce3b18c81 | -3.54463 | -54.74234 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52ed9248-b3b3-39cd-a8cb-b8c25b6cba7e | -3.5383 | -54.74158 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d632a46d-69b9-3a22-8810-6d407e270fac | -3.11602 | -54.16451 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70526c29-cdf9-345d-999b-1a5a0c4936fb | -5.0763 | -60.21814 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8a7f4db1-bda0-315a-88ef-dbafdbc13cb9 | -3.73595 | -57.15978 | 2026-10-10 05:48:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d8d6823-c0bd-320c-8197-e334dddbeb9c | -1.33505 | -56.3973 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b059f988-5c05-3814-9830-d9d8210dca92 | -2.02305 | -61.26655 | 2026-10-10 05:48:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01962f7b-ccd3-3d60-a99d-017b79a1720e | -1.21935 | -55.65354 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dfdca96-6c4a-34a9-bab2-98c79ea2bbcf | -3.93663 | -55.72788 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b00e2d12-e274-3dbc-a8ee-459c62701e3d | -2.61203 | -59.98495 | 2026-10-10 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0f46529-78da-33d5-ac98-b3e37c763a63 | -3.49873 | -54.61 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5adea0f0-9117-30fb-b22c-d68ac2d41de9 | -3.5764 | -59.08121 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a8f4df1-5744-3962-809b-095ea687f3a6 | -3.76325 | -58.84334 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fa6efc4-a5d1-377f-adc3-0a12a30f33fe | -5.22282 | -60.04398 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6d3a10f-d29f-3319-9b1f-d987b6081378 | -4.3813 | -55.161 | 2026-10-10 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ccd1e48-c3f0-360b-aa7b-5ca557d812e3 | -3.84551 | -55.78624 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 75a05be3-d910-3700-967f-9f4b3e32228b | -2.46864 | -56.06112 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14b781a1-1555-3c8d-8626-65496fa5777e | -6.36386 | -55.16033 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ceacfc04-4e21-386c-bf3f-0220d3d6fc29 | -3.53081 | -59.57478 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20a6a52f-e00a-3d85-b270-0818becc6e8f | -3.19954 | -53.85577 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a349f4de-8bc0-3d53-9109-cf8cf6ccc8b8 | -3.57601 | -54.38573 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e3da568-6bb3-3eac-a8cc-8a1dfe3fe36d | -3.98669 | -59.35285 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8b30df4-82eb-3b93-9c2a-1a09e8df438f | -1.21406 | -55.65646 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c67b7e66-7fe4-30b3-8eb3-18a6392bc3ef | -3.12254 | -54.16534 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9dc11fd-e9d7-37a7-b8e0-62e423f96bd9 | -3.18886 | -60.04689 | 2026-10-10 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6afd4ece-408c-3bd4-9788-2fd4a9c37838 | -2.39374 | -57.89765 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dde065eb-2ed9-3026-8a6e-24e4cbef7777 | -3.57716 | -54.69572 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e892026-07a0-3124-aca9-856cdad788c8 | -3.74521 | -55.94817 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9ebcbbf-7393-3d7f-89e7-957678c8befb | -3.90595 | -55.90025 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a48cca4-4f6f-3b0f-9046-6417d82ff6d3 | -3.98915 | -59.36826 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7ce2673b-9f68-3868-9c94-7774ca9a7500 | -2.92295 | -54.07668 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7764461e-0ea4-3091-9379-82c3e2d505b3 | -4.12359 | -54.04134 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06792823-6b79-33dc-8a5e-e66918ec01e0 | -1.21363 | -55.65248 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 808be3e2-19e6-349b-b301-fbafb7d3d715 | -5.08013 | -60.22327 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b3af279-d43b-319b-b82b-e4e29e71d56f | -1.45238 | -54.47337 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19696b60-9ee2-3a97-85c5-76a501364c62 | -3.3055 | -54.00792 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| abf1d710-d325-37bf-977b-ca7e6c8d1fd8 | -1.60511 | -55.15964 | 2026-10-10 05:48:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c96fd40-4d7d-36ac-b71c-3680ba788f60 | -5.96933 | -55.34307 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| becc9274-5bef-3771-9414-9210be1cd795 | -3.44108 | -54.54215 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6486f845-7b15-348b-9a99-c7a70f349894 | -3.78066 | -58.5815 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bea7a05c-2436-368c-b649-da8067f804af | -2.84642 | -59.12247 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eacdbd77-c033-3b02-91fa-9c2dabb365bb | -3.60324 | -54.60564 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb4f2c1b-c500-305f-ad89-6e02a3f2f151 | -3.8699 | -55.98518 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 876f0295-bb88-3a87-85fe-a6dbbb301e37 | -5.99857 | -55.3636 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e68427e1-d988-3a18-a5b8-58478dd65f48 | -3.49562 | -54.61454 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0235379-837c-380c-a520-473cd4736cd4 | -4.10436 | -56.1326 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2649e6d7-ebc6-3a0b-a0e3-ed26714ab003 | -3.28531 | -53.87109 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6ae6e5d7-43dd-3217-a691-44fa8d097347 | -5.07311 | -60.22011 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34b95f9d-3f49-37d7-8c9c-0665ddae2551 | -3.57824 | -58.6322 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51089a20-5d3a-320f-ae3d-404fd1c84e14 | -3.5688 | -54.38419 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9633d3cf-6d00-3423-bf15-88688ea57832 | -2.39418 | -57.89474 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c25454bc-2487-36c9-ad0d-ebda7529f7e8 | -2.38826 | -57.89975 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95e89f81-ee62-30b9-b677-ab849b502668 | -6.12225 | -55.7006 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4e3f9d3-06bd-31c3-ba3a-a7a5d109f99c | -3.73117 | -59.45976 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b69f04d6-06e7-3729-91fd-03ec4344aee9 | -2.89044 | -54.07152 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 270b8186-9745-3e24-b10b-7ea93a29f491 | -3.95991 | -55.34623 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18b435a1-869c-3260-8f9c-ee3057dec336 | -1.88537 | -54.6846 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d834582d-3b5f-39fc-8083-491d2b870617 | -3.79051 | -59.37165 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e4b9892-2535-3299-a281-c2ac81936cbb | -2.4241 | -58.00031 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 323727a4-4dfd-3f4d-88d3-45fd2a8307a7 | -1.11319 | -54.17481 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35bc1617-7348-3274-aeb2-2f5abc90ea49 | -5.18554 | -60.30521 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7157aadc-64bc-3395-ad3a-8cbcf1378d2b | -1.9668 | -54.38481 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14e7a001-7f22-3259-a56c-6e71e0dfd899 | -1.88756 | -54.67027 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2951cc45-1ecb-369d-965a-eca344821d2e | -3.51866 | -59.94884 | 2026-10-10 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68f70512-c0fd-379a-96c6-d91ddfada6fa | -4.82266 | -56.08574 | 2026-10-10 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a434a7ff-682e-3cc6-a92a-8618046a2918 | -3.56377 | -54.69898 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65649404-6b53-363b-9cbe-29bba3614167 | -2.60965 | -56.48436 | 2026-10-10 05:48:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5200cf7-0713-3e97-868d-d4911ef99ce8 | -3.55818 | -54.69297 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aecc700-48fd-3215-911f-f16128ef2ac6 | -2.73397 | -54.14224 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76f8e5a1-6465-30ce-bdf2-2826c53f2985 | -1.63276 | -54.43762 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d3640c6-8752-33c9-b5af-3080364634bc | -2.51449 | -56.14462 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87e17d22-b0c5-30b4-bbbf-c46230f1eae7 | -2.9961 | -53.89996 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58853410-bd4f-3788-b980-656c722ad50d | -4.1222 | -54.03687 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f437f60e-f51b-3c53-9283-8b119e802f92 | -5.18617 | -60.3008 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c92cc3aa-64d3-3990-b23a-e484bad46eeb | -3.98296 | -54.46214 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README140.md)
