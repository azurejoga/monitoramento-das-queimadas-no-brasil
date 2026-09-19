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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6608549-5bd2-3968-b76c-c74c6833dbe4 | -13.38717 | -48.03489 | 2026-09-19 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| be0706d8-c0c0-380a-a3e3-08dc2b147769 | -10.81962 | -50.17094 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2f12d00-3095-3559-aa76-744951e62fb6 | -11.32264 | -47.35962 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d1e6e56-a926-3d78-81eb-ca357dc44147 | -11.12155 | -45.29866 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c3af0d4-06ee-35b6-a8d8-95b07414822a | -11.55622 | -46.89727 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eefc4fbb-9926-3b23-8eda-98a3e9fa493b | -16.79786 | -46.99391 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5b551576-9ed3-3806-af9a-380245214ebc | -12.86514 | -46.34504 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a59ea6c6-6a37-3cc1-88b0-65d8c4885d92 | -13.61081 | -48.30159 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1f92a63-9edf-30b9-b1a8-ef2b77bc12c9 | -14.15748 | -45.16851 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1db5a664-e251-3dbb-9069-4389a4bda93b | -17.03811 | -47.29399 | 2026-09-19 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf8b3fe6-6a9d-3d36-93f2-c182893280db | -14.92654 | -49.91776 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9bb2be58-edf1-31cb-99d5-b373f3987927 | -11.41949 | -51.45238 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63e7e9a6-68e0-3d05-8f22-462247b8ed8d | -13.61024 | -48.32896 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30014f04-61b4-348b-8ea0-195d26fdfc0e | -11.08438 | -48.29302 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9ce357da-d4a8-3beb-81b8-f8481c71b854 | -12.99813 | -46.98079 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b0d3b9c9-063e-3cb8-8c4a-13411e3ae4e5 | -11.37546 | -47.03728 | 2026-09-19 04:04:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfc3a254-3477-3c97-87ee-c49fd743f75d | -11.06459 | -48.27136 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a7c05f7-6dbb-3029-8d08-a9ab315a7d12 | -10.83077 | -50.92921 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b28da9e5-bcd9-32bb-83d2-be8f6b231b05 | -11.97416 | -44.99422 | 2026-09-19 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de5730e2-88eb-36aa-96c2-c1be2426ed2c | -11.11479 | -45.29268 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ae72f4-e906-31bc-a779-110793a75b8c | -10.84452 | -50.18238 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a0230bc-5986-3b35-86f7-f2dda2903a34 | -11.11695 | -45.30279 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87362c04-5b63-304c-a8e2-1e27e15d64ec | -13.60836 | -48.31533 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c704acb2-64aa-3dea-ad6e-db693ab47f6a | -13.65072 | -46.94284 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35c8f7cc-eb28-3b9a-b092-2c96b0fca7b5 | -10.97854 | -49.70396 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9b18803-470e-33c3-b220-8ebed6d8faac | -12.97274 | -46.9833 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d35d701-50dc-33c3-b6b7-ea47f200f52d | -12.69138 | -45.9478 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4e0a9eb-34b1-34ae-9985-59fd1fdffbe5 | -11.12615 | -45.29454 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb3c75e2-01c4-320f-a756-bd442dbfff36 | -11.06545 | -48.31933 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 42d96112-2620-37cf-a8ed-0e4ddfb6ddaa | -17.95789 | -45.12578 | 2026-09-19 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6cc019d1-caed-39c3-b3c2-271b46b48b2f | -14.92692 | -49.91567 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0f9985bb-b061-3f23-8c48-714258b30b5f | -13.23544 | -46.94308 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52ff8729-2f6f-3c3c-bf57-afb0f9b116ea | -12.12711 | -46.97684 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 393e8f9b-2db1-3b1c-852a-08d28c88c180 | -12.28479 | -49.1651 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| f9642fad-46a4-3b06-aca5-4cdfde119f1d | -11.94549 | -50.11933 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e6fd4bf-3684-3ac9-9e53-1be042536778 | -10.70149 | -50.25292 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 068b24b2-def4-3bcb-811e-43dda23cf14f | -11.12453 | -45.30404 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 005ef118-2b73-396e-9be1-75f69223dc86 | -12.27905 | -49.16943 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 4e512537-215b-3957-a96e-abff73b5aac9 | -15.03022 | -48.57919 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c60abe2-cc03-3623-87b7-c3f8c4339f1f | -13.73994 | -48.79187 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d041fb85-f6a6-3c4b-8345-5d1efdc6a57d | -11.31033 | -51.73158 | 2026-09-19 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a11b8239-0c64-3b28-959c-c1fe07b6795e | -12.16697 | -46.96819 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c787838-19b0-3fed-a74f-88c2e6f60253 | -12.58688 | -49.10397 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 0f353480-3aa3-3227-afcf-fd03041d484a | -11.87934 | -47.61467 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 455667d5-8425-3be8-a670-5726d3ee5936 | -10.86402 | -54.09909 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb9ec058-f2f1-34a6-a70b-5f1611dafe46 | -13.61197 | -48.32051 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4453b931-57c6-3f9d-b9d9-6529a279de70 | -15.03191 | -48.57008 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7ffed1e-bdbd-345a-85ce-ddecf5010f18 | -13.63645 | -46.92997 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00321e20-2260-3024-9c13-ee23f8309baf | -13.01535 | -46.93144 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5b583af-6dcf-3316-8e48-dcab9a8989c8 | -15.64743 | -52.71347 | 2026-09-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 679e5e00-6b76-3f0d-b41e-3e4358afe882 | -13.88227 | -48.59727 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ec2f77b-0f16-339f-b41d-622fe435d740 | -11.97872 | -52.4571 | 2026-09-19 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 956c2603-b274-3846-a4fe-0e53b8f45d09 | -14.10121 | -44.83095 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b68fe0f4-0515-3a2f-92c8-acc8e5041e88 | -11.97719 | -44.93129 | 2026-09-19 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e98291a-285d-31e9-9c85-d2a29edf2a99 | -14.95718 | -49.93816 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 606b12e1-f90c-3cf1-b688-305ba6f823b9 | -10.27618 | -50.00663 | 2026-09-19 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 935b62d1-a8d7-398e-a6dc-7e6dc31d25b7 | -16.79876 | -46.98891 | 2026-09-19 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6aedae13-1125-3da9-924f-5ea26c8e704c | -10.99726 | -48.32853 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5926df37-a1d2-3a47-91aa-c59a021a369d | -11.79887 | -46.82619 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7b9c700-b35e-38fb-8d24-6e24987fb565 | -11.17979 | -45.38885 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8173725-8b06-3a9c-b8f7-f90f14a5b1e6 | -13.87497 | -48.59647 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c50408fc-685f-3041-99ea-3dbff015ad91 | -14.92953 | -49.92756 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b4a8d8b-b321-328f-9a66-ba0955810795 | -12.70373 | -45.94493 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5aa5566-9d71-31e8-8a51-64ab2c27b04d | -10.88801 | -54.04951 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 804a4a29-a3fb-3d9b-886a-0eb1e294be2c | -10.89463 | -54.05084 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2b540bc-8b16-3c23-b1c3-53bcb95c5301 | -11.8786 | -47.61889 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73b647a2-ac21-3d24-9f4a-83d1af575549 | -14.93132 | -49.91865 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06b1426d-5de1-386c-affe-384f803648a0 | -14.68739 | -46.65818 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 585f83b5-660e-34eb-986f-4db0e7c821ce | -10.84854 | -50.18985 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb2cb6ca-5992-3dfb-92c2-3d4f365bca72 | -13.6461 | -46.94545 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1acf9d4f-e186-3312-90ee-6b32dbadf772 | -18.68298 | -44.61381 | 2026-09-19 04:04:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c91f037d-23a7-31af-b02b-246876314a02 | -12.74431 | -47.02121 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8796557-e552-3b86-8f3a-e0a57e8ada6f | -16.59883 | -46.9969 | 2026-09-19 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 066d67dd-3c74-356e-8c72-5da4d7f9dddf | -12.12692 | -45.15465 | 2026-09-19 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35b22a68-77aa-38d5-afd8-49b880bd82f1 | -10.83483 | -50.90741 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5de61cb0-f79c-3a5d-b8d5-a59099af5b6c | -13.6107 | -48.30226 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0fd2c30-a88f-33e1-9f95-5553e106bcfe | -11.33327 | -47.34958 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9f68944-ab35-33aa-a340-880fe7a8132a | -13.60753 | -48.31996 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6745f25-3bc7-366e-89c0-758d844301b3 | -10.88093 | -54.06452 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eae494f6-8b16-305e-821b-641360ef6ea2 | -12.58366 | -42.22351 | 2026-09-19 04:04:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00824588-c6c5-398c-83b7-2872bc1588fa | -11.30826 | -46.75362 | 2026-09-19 04:04:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5edd15f-b621-351d-8bf6-cddf72d18f0f | -13.00613 | -46.93617 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 024eb066-0c46-362a-bb01-b4f245d28bae | -10.87903 | -54.05966 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0980e981-302c-3e18-b654-ab928ec90ab2 | -13.88302 | -48.6029 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5c1cb93-7a4e-37f8-b4fb-1c7504bc7e96 | -13.23665 | -46.91294 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb72b776-c20f-30d8-9865-9945f5a9a4ea | -11.34031 | -43.40907 | 2026-09-19 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e6ab396-948a-3c69-83d7-556b79855928 | -10.82023 | -50.1677 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b30924db-f222-3bfa-a3f2-58e62f1328fd | -10.45714 | -48.68283 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a145debb-c8f7-305b-8377-fafd4632b6e5 | -13.00616 | -46.98288 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3232c079-3db7-32fd-841e-6c850a79939e | -11.94269 | -50.10604 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98866a26-1f77-3054-bc31-3ba56129186b | -11.31643 | -47.27077 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2108e55-a0d8-30f1-8e33-69cf4c8cd360 | -11.06341 | -49.77385 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c918c9ba-c4e2-3f29-a571-bff3acb4faaf | -17.68326 | -43.97878 | 2026-09-19 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 088ece3c-8a44-331c-81ce-bbf9362740a7 | -11.3741 | -44.10711 | 2026-09-19 04:04:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aa728ca-bcd9-3848-818c-8677522c788d | -12.98591 | -46.97864 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfe62b52-7ab0-3e5a-bc08-ee3fdb8cfc76 | -12.28578 | -49.1598 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 66e2ff1d-c5b3-3f14-a094-69b513c8312d | -9.69922 | -54.82707 | 2026-09-19 04:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5af662e1-9502-33b9-b254-b89c15e14d63 | -10.45257 | -51.23484 | 2026-09-19 04:04:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65c0e1c7-d9d4-3242-8402-87a49d5a374b | -13.60751 | -48.31921 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 05a7769b-ec54-3111-962f-0236157eacfd | -13.87943 | -48.59727 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README42.md)
