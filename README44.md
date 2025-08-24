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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76183e47-b705-32a2-bf00-f45fa33ee178 | -8.92111 | -62.44365 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8e1fa92-cddd-3952-932b-365b00ee2bcb | -7.80966 | -46.62542 | 2025-08-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd668357-d8ab-3c28-bc87-2aaf6e5a756c | -6.88959 | -45.68889 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52fb4918-0190-3943-b805-b687711799c9 | -13.62018 | -48.16821 | 2025-08-24 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb0bd491-e3e1-3e57-bc23-744d785e6d76 | -10.54663 | -47.13939 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0396ba1f-e4f8-3478-ae36-ffbcd18ec798 | -13.10488 | -44.10139 | 2025-08-24 04:34:00 | NOAA-21 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6883694-6118-3d20-abc7-37723b461569 | -7.35299 | -43.85243 | 2025-08-24 04:34:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dca9a96b-00b2-3126-acf2-39ebfef157fe | -6.43568 | -53.38742 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3eba3e1-2902-3bfa-a861-6458c8968267 | -11.13951 | -44.78527 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb12e1c0-0cb8-3f93-b049-f85092aa049a | -9.68298 | -48.34903 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d15b80a-09d5-35b2-b328-7ad98c786bed | -8.85806 | -52.04955 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1be81d74-ecd8-3210-85a9-5dc4dd93aff9 | -13.04018 | -45.22663 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c83f9f5b-3ab7-347b-9909-6d3f4ef204fd | -9.19529 | -60.7848 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2903461e-4de3-3c86-8055-198a921c53a4 | -8.93423 | -62.43866 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4db6273-afe8-369b-aeef-8fc148d39bd5 | -13.04086 | -45.22179 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 038bd8ce-f9c5-311f-81de-edfaaf299010 | -11.51222 | -51.86164 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9165e455-7b5b-3692-aad9-b8c7ad4589ee | -7.92703 | -45.91769 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8bbc7b6-9c3c-3aa0-9a02-d2820e0230cf | -11.54552 | -51.90345 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b70f428d-5c39-325e-86f7-71feb4f57f59 | -12.99417 | -45.21983 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1d8af74-5ffc-3c0e-b600-467b4952dbc0 | -9.51294 | -60.51105 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9575950d-065c-313c-bcb9-1cad21fb6cd0 | -7.65846 | -46.25803 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f454279-1d15-3cff-9a38-f5e3c77ee62e | -13.49389 | -47.02408 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d1d6cbb-dd4e-3caa-ad2a-043af41055af | -7.17452 | -44.66592 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb3fa708-32f6-339f-b5e4-cfb6145c9ebf | -6.462 | -53.4003 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b1f8712-98e0-3ea7-9171-349c45c33ee8 | -8.05916 | -45.00488 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57aeae5c-fd06-30f2-a2ae-21008785d740 | -5.45035 | -60.19186 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee483b86-b11c-3b62-a3ed-acb21f6b8655 | -11.52546 | -50.48566 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9882ab8f-3818-3170-9f38-c4d6373d69fc | -8.8957 | -62.42459 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aaf1f043-1fa8-3495-8948-c4d211a5b28e | -11.51156 | -51.86566 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b4112b5-4b6e-35e3-ab69-4f1ca05391cb | -11.3353 | -47.85686 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f458bb41-95b1-34e8-94ed-4444f8c7267d | -11.11197 | -44.78593 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b4d09b9-ae6b-3610-8e5c-8f4b23f917da | -7.62314 | -45.2417 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 873baf7c-8cb0-317b-8440-585dd4774a27 | -5.8772 | -57.75758 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fbcb19f-264f-36ca-b254-45e00c3da07d | -8.91243 | -62.41358 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3c48704e-eef3-3ee6-8565-07046d718093 | -6.57375 | -59.87149 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 732169a4-dca0-342e-911a-c85686655f01 | -8.60735 | -62.59695 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a733b773-fead-3a35-8963-28d0e8b7c424 | -7.44542 | -57.62228 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a09f713f-43e3-39b4-a609-d02afd5feb0b | -6.89598 | -45.69384 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3149c63-b5e0-36ca-9a16-134612708f17 | -8.76687 | -49.98822 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da1c2fa1-ef08-318b-8163-a1b927ae97ab | -5.42827 | -60.16525 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67d36cc8-7f23-38c4-b414-4c4821d63747 | -7.74988 | -47.35184 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11d8605c-9dc6-39c4-8678-8a6273f0442c | -10.60392 | -44.32442 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6a0da34e-0c10-356e-bf29-3240fef3fc58 | -13.47211 | -47.02599 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1fbfd57-63df-375c-8120-00b9af7d7292 | -13.05414 | -45.23858 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7aeb0bd-3b27-39bc-a615-3e659b93a53c | -11.54298 | -51.85364 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77d43aa6-791e-3500-b3aa-382b89b5961c | -9.1791 | -59.46462 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c7bdec69-ebeb-384c-95ed-6c8ec6e71584 | -8.85732 | -52.05407 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fcd83d7-0575-39d0-b628-0bd61e0b5a28 | -9.16504 | -59.59415 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c91a9a4-ecbf-31ca-8d69-55d50b3ddeb6 | -10.41341 | -47.18794 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3148b9d5-0aab-3782-aaac-0c2f65e20a47 | -8.76019 | -46.73844 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05381cb0-00b4-3439-a4b5-b702bf61f910 | -5.74779 | -57.58883 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| afe8cc0b-bca3-3666-a255-133f0056a064 | -11.05616 | -44.61045 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eddd3483-7fe3-33d3-9372-418d914d3e34 | -9.16564 | -59.46452 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fcd68d93-6bf7-37ad-905b-68d51e8f3ac6 | -11.32522 | -47.85541 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c83b11a-6635-3d7c-9235-8e933e530f56 | -7.43344 | -60.62438 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad62b9b0-52d2-3eba-971e-26291d49db66 | -10.41396 | -47.18423 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 98261c7e-17e2-3260-ace2-85bad82b4724 | -13.03635 | -45.22605 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f101aad-c373-3252-aadd-593d0aa549b6 | -9.19747 | -59.46376 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 246b8595-08db-39f3-9b4b-3d25042a0672 | -13.6241 | -48.16504 | 2025-08-24 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7244baa5-90a6-377f-8e38-e049afec32d6 | -6.57915 | -59.87741 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f15484a-af51-3c42-836f-6f79364e3031 | -10.40606 | -47.19052 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c3280bb-d342-3562-bc67-7a4b849bacb1 | -8.04014 | -47.34248 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e2b6e6-8cc1-3b50-98d6-a960dab9738e | -7.65337 | -46.29162 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89bac9c4-2d95-3048-b80c-5c7bd76082b7 | -9.14839 | -59.49893 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0671ff69-2f61-3b0d-8913-601739db9c53 | -11.70369 | -60.18297 | 2025-08-24 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57067ee0-2786-3e49-b5b6-9de15aec19ea | -11.51721 | -51.87811 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a152656-5574-3642-b306-f061f17c82b1 | -13.04223 | -45.21207 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0ddacb5-d5b4-31f4-8c17-414defa92b44 | -10.48935 | -46.81923 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d656c225-4462-3f29-a8d2-c687610025ba | -11.28427 | -44.93302 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1be596bf-e478-325f-80c4-ba61d2043e37 | -5.74762 | -57.59044 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5867196-604d-3ba0-8bcb-9a395a8e40fc | -11.53246 | -51.85177 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a0aa31e6-a0a3-3b70-9e0b-7edb15078118 | -11.51086 | -51.87289 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d76df8-93bd-35ef-90f6-c95fabafefb0 | -7.59756 | -46.24467 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d0077fe-baef-319c-a9e7-f834578e62a5 | -11.52808 | -51.92123 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23cb4722-2c66-3be1-8aad-1a939a15eeaa | -9.11621 | -45.19076 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccb288a4-6ce5-3084-8ba3-4382474fbb83 | -8.90137 | -62.43279 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bff4ca4-4e0f-3400-8cb3-acac823c04bc | -9.16175 | -59.4926 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| daf99597-4cc2-3ff5-8b47-ec2fa3de80c1 | -12.998 | -45.2204 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51f7662e-e5f3-3d19-b440-88cc4983d1fb | -11.33303 | -47.84922 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 711bf01f-3c03-392c-b9dc-dfa5be8720fd | -13.50034 | -47.0291 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cec71e4a-4162-3569-8caf-99da6ec0670c | -9.15212 | -59.44653 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e670c2df-9697-37f3-9ff3-0d529d9ccb79 | -6.61496 | -48.04683 | 2025-08-24 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2db2e18e-530a-3c19-a95b-401f79e5dc0b | -5.80024 | -59.22595 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db968c6a-397e-3a4c-ae03-f5b6bbbca821 | -10.63478 | -51.61305 | 2025-08-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aec5ecf1-a80e-3ccc-8e00-a36e5fe81b11 | -6.57286 | -59.87631 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c80b06f6-c8d2-3db0-9cf4-76fd3fc4fd40 | -8.90332 | -62.44718 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| da0cefa8-01ce-31cf-8540-0ae8f816b7d1 | -9.02989 | -47.64548 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cbcb56e-7c6b-3115-b499-557265e43bc8 | -6.88903 | -45.66906 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 945d00c5-249a-3560-b7bd-c2bb12c7afb9 | -9.14998 | -59.49046 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 187d1fcf-5953-3afb-9d79-727111dd993e | -9.16482 | -59.46876 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf1794ab-93f3-3338-b947-3286e3c389dd | -11.73507 | -51.6988 | 2025-08-24 04:34:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edd33148-4d80-3119-9ac5-3dc445a70a6a | -9.8017 | -46.4278 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52147e54-151c-38a7-92b1-8c61774d0926 | -8.90002 | -62.43966 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bde8891f-dc8a-3fba-a44c-08abbca0af70 | -9.0291 | -59.01246 | 2025-08-24 04:34:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd551c15-3c09-3c86-b075-167a53bc70f9 | -13.3712 | -47.48378 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad76a399-2258-3d01-a6d9-41caa76f24fd | -10.60784 | -44.32499 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 6a256c1c-bb0a-34d1-8f56-034cf10f5cb3 | -13.46621 | -47.01717 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17fa35b6-5150-376f-b53f-e0307294e355 | -9.14815 | -59.46772 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9e6000a3-540e-35dd-82d4-c456a585a0ae | -13.67145 | -47.9862 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9e2fc75-89b8-340f-89eb-18526381db6f | -7.60153 | -46.26456 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README45.md)
