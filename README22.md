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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38d9d3f9-10ac-3175-81c7-4d9ccbbb02a9 | -3.15552 | -50.44316 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9dee6b14-3bb3-3e8d-bfba-1873e1f59675 | -2.94365 | -54.13194 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41171746-6c8d-320f-8b18-c37f45983d8e | -3.33125 | -53.38841 | 2026-10-05 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a2ec25bf-a1ec-30bb-86c4-2ac61efa84d9 | -3.9048 | -49.71271 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68281b38-d0a9-3754-a24b-a8202ed7a7af | -3.46061 | -54.59636 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 88d0b093-f83d-39eb-aab6-2512f333255c | -3.1352 | -53.72941 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5040254e-a21d-36ae-a06b-22ec1323529f | -1.09891 | -54.11287 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78d3ccd1-594c-3b25-8dbc-20ba9e4fc5d9 | -3.11728 | -53.75598 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ebbac2dd-f29b-33d5-97ac-38280a755df8 | -4.28434 | -50.27297 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03c9e187-4ae9-3376-bb73-4c6931adfdbd | -1.08339 | -54.10677 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6247f8a-2847-35f8-953f-67a04ff0f5e0 | -3.048 | -54.21075 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b8ac476-23aa-334f-b82a-0ecfc588cd77 | -3.11499 | -53.72602 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ba4329a-ac51-3207-aad7-7dce2b3c4f46 | -6.89713 | -43.67477 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dfe6a37-b8a0-3c98-b328-ac7354352a05 | -3.11823 | -53.75014 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0a0e579-585a-3919-b3ea-647ffa0880f9 | -3.27785 | -50.40523 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b8c170d-7273-3640-8049-6d393bf0ac3b | -2.80993 | -54.12968 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41556b67-01f8-3ce6-b496-12a84d267677 | -6.00872 | -53.52139 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcf5c732-fc8d-3672-b04d-541000e9a0b9 | -3.86402 | -55.82833 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1118e6d1-9e73-3682-8e60-e8e7cb3a26c2 | -6.41824 | -51.96264 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b81a7e59-7520-39ba-86eb-a986fa1ea494 | -3.87957 | -55.80678 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f1f9c6d-a7df-3230-afd2-9b4d0ec89286 | -2.94884 | -54.13288 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dea8c4a7-532d-3094-9334-8f4953cd20e7 | -4.53008 | -49.69422 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa275c4b-7d30-3902-a5e3-cdaa4b5dde57 | -2.78122 | -54.10878 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50edf92c-1018-3685-92c4-857c37c6b53c | -2.96843 | -48.92233 | 2026-10-05 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3dfad9e1-7374-3f74-935b-aca69940f080 | -3.07008 | -54.17568 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| a1987920-bbad-3388-96fb-4d41fb795cab | -3.06644 | -54.16549 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9adb76e8-7694-3524-9d54-9ae7a3795470 | -3.11919 | -53.74427 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aa95b07-fe8a-3f99-b39c-fd000e69b942 | -7.71868 | -45.45828 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a22b7e6-de84-36a1-ab9e-f0fb032f5d12 | -3.04749 | -54.21721 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90162e31-6772-34ed-9d3e-861da1c32d49 | -3.31931 | -53.84926 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f68441f1-26f0-360c-9a4b-86c12635a2d4 | -4.28041 | -50.27232 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c79dbe3-b9cc-3dca-b9ad-89bf533f1ba8 | -3.07212 | -54.19528 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f093123-cc6f-3b16-af4b-2764eaf65af5 | -3.11386 | -53.71328 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99a7ae43-d228-3ceb-b38d-73dd58c27ae7 | -2.81514 | -54.1306 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 185bfe09-3770-367d-99ce-567365724e8f | -3.1241 | -53.73352 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0d47fe0-3a62-311a-8da7-2e4470d7e841 | -3.12187 | -53.75977 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7f82874f-fca1-3eef-9e09-84fd4eda6c36 | -2.98597 | -54.04 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a2ed428-2d3d-360d-b890-438157094aee | -3.13619 | -53.72358 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f6b8f026-a6b5-35ed-a694-c1a99d30c555 | -6.91125 | -43.67159 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98346571-f927-365f-acaf-809b22bec464 | -3.11365 | -53.74634 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7fd15f-2770-3b3b-8d74-2c4883db8321 | -4.28989 | -50.26377 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fff0c24-1183-372d-bc74-dafe228ab29f | -2.94228 | -54.20286 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 396d3545-b399-3d93-8ef5-20533e3c1fbc | -5.68435 | -53.50136 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 863d3d2b-d1d3-3c76-a732-257704c20c05 | -3.11955 | -53.72976 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb5c512c-849c-3fb8-b427-5d1943cf23e3 | -3.87317 | -55.80966 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2c3ea0a-ead9-371e-a2c6-2dc042f5e892 | -3.12468 | -53.76069 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b39aafb8-b918-3b03-a33b-9fd7be072d75 | -3.30764 | -53.8564 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a98f3278-487d-3d1e-bc09-bb00701e988c | -2.98227 | -54.09349 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d6ea7a5-5703-3455-8c7f-b98c0278d450 | -2.80158 | -54.1153 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bc8a523-2493-37b9-adce-0f2759311ad2 | -3.59479 | -54.31028 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50ba32e2-145c-30ac-98b4-5e7a4dfd1246 | -3.51953 | -54.62333 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 489dbf86-89a1-3417-8c07-efbcfaa24e2f | -1.47203 | -46.27183 | 2026-10-05 04:38:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73c38339-4f67-31b8-aaa2-375ee54a7cba | -6.18046 | -52.93251 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd5a2bb4-8a06-3562-8336-db8f9ef1fde2 | -3.37818 | -54.10334 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a5699a5-fc49-3cb8-ac41-3705e46c6f45 | -3.40646 | -51.80626 | 2026-10-05 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c41ca7f2-8f5e-397a-acf8-9d7af1a39c0d | -2.7974 | -54.10816 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1875598-ed14-3c0e-a8b3-af0be67ad3c5 | -2.80627 | -54.11932 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 536809f9-d0a3-397a-804d-b535d6b3b456 | -2.94472 | -54.12568 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7f28686-e09d-3c30-a1b4-579eab1c44d5 | -2.94683 | -54.14319 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 05114644-fe8a-3ac8-b0ca-244009f11ca8 | -1.5562 | -54.7953 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37cf3f48-30d6-3a66-ac06-f57f4532c031 | -7.26604 | -44.29911 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2db6f2b-6ca2-3d3d-8a98-db2dc2d97e0f | -2.48301 | -56.10583 | 2026-10-05 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a19e598-3188-3b9c-a403-76f20a9ff23c | -3.40002 | -50.1477 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 205bec9f-fa0d-357e-8fd5-411c04014eae | -6.89774 | -43.67078 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48bc10a6-bd16-3347-bd6c-ac8f6370fbb3 | -4.11589 | -49.06672 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b8052b4-e71b-3bee-a5cd-97bdcf63240f | -2.80916 | -49.87139 | 2026-10-05 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a3b74d4-eb5d-3fd6-b1d7-3881c115be12 | -2.80888 | -54.13604 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80fff200-b584-347b-9d98-bc20dcc01a00 | -3.51545 | -54.62944 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a4a6e4c-9458-3775-b714-12c077691934 | -6.90962 | -43.66439 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0852d449-5acb-37e4-a247-d537cf3d4191 | -3.50588 | -52.95662 | 2026-10-05 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c1e9b0-c3c2-384b-853f-ae33679161b8 | -0.49612 | -49.10282 | 2026-10-05 04:38:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 092c8097-0897-30fc-86a7-16ce773e32ae | -3.12062 | -53.73547 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d799100-b274-3239-9766-338ec842730e | -6.89882 | -43.68719 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d41d965b-5dd3-3bb8-beb1-4e5d6e844f1f | -3.50696 | -54.61432 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 357d9535-0d54-318a-a5f3-bd95728656a0 | -1.51888 | -54.8235 | 2026-10-05 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7280a86-0647-38d7-9c47-2b367327b119 | -3.11349 | -53.73477 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 773b09e4-ed77-3b87-9301-3088f62ea700 | -3.05324 | -54.21161 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a40e8d48-cc98-367a-8ff1-15f21d1b949b | -3.27813 | -50.01668 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f4c566a-3158-343e-90dc-7e50e5d41ca9 | -3.30159 | -53.84579 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02756c84-5558-3ca2-ad68-0342e257dd0d | -5.95327 | -41.34003 | 2026-10-05 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b07bb33c-b7a0-34a6-ab6e-38a5627999ac | -3.18565 | -50.53884 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18d8743a-ba99-3598-9b21-ad02322559c3 | -2.44366 | -56.38029 | 2026-10-05 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463db310-4d18-367e-9dce-32b8bda58efa | -3.46819 | -50.10234 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b022956d-8168-3dbf-a88b-f5e34ca67f4c | -3.10208 | -53.75344 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c687b00-c33b-3e95-bf74-d1a0df056661 | -2.9041 | -54.14226 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53e7307f-aaf6-3014-b5fd-3edba06d5a51 | -3.04478 | -54.22965 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 832dd6e7-f60a-3313-83d0-69fd8afd3ef1 | -3.0675 | -54.15929 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 59f67290-b882-38c4-88a3-e89214df7a3f | -4.07841 | -48.95768 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70787c05-976e-3c33-b01f-698996e057be | -3.31078 | -53.85341 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05539c57-2217-3d0c-ba89-3554e77c8596 | -3.80617 | -47.48613 | 2026-10-05 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2495f7-77a0-3cff-aadc-963c3eef0ffa | -3.11199 | -53.74353 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d8d7844-73a6-3b34-98d6-50e3f08d3646 | -2.16149 | -53.6641 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64b015e-c9d6-3f63-b83f-3418832cdd0e | -2.90045 | -54.13194 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f955872d-8418-332c-aec2-174c5c91eb55 | -4.28595 | -48.5693 | 2026-10-05 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74c0551a-7d3e-3b47-910a-369b596bd8a1 | -3.04698 | -54.22037 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74548c42-f358-3c2b-ac9a-d37217ee6200 | -2.58192 | -51.86984 | 2026-10-05 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e801efb-69da-3cdb-bb3f-ae228c0a749a | -3.70257 | -50.65189 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b36b0f7-9cae-37de-9977-3df3fd742fcd | -2.9859 | -54.10362 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aaa4b159-fd5b-353b-8b74-89fc9e213d1e | -2.16327 | -53.66824 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34c3a442-cb0a-31f2-b929-1177a2557c64 | -2.96837 | -54.20775 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README23.md)
