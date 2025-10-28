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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 145299e6-17b0-3950-8e7a-7f8ee0b02833 | -14.42077 | -47.85812 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a099d31-bc88-384d-a824-e0b3c51bbf8b | -10.57349 | -49.80116 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c0cdb02-c74a-3076-9307-f0497b20dc86 | -9.97964 | -47.16179 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 026269f5-be27-342c-9804-2c71aef45296 | -9.51227 | -40.31483 | 2025-10-28 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 77d59dfe-bfc2-3901-8534-2b6c3b476c04 | -13.24653 | -47.06411 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 788636d2-f4c4-310f-a50a-413935f3e625 | -11.21746 | -49.76812 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2311fe22-ab06-322b-a198-8f84747f444f | -14.63937 | -48.40387 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ab88737-0566-3dd9-aaa0-ff8b2b654d84 | -11.28801 | -45.51552 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1fad691e-0c71-39fe-a9be-de9db87d023e | -12.85166 | -44.64557 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ad2f4d4-86ea-331f-834d-5800c0b5071c | -10.57903 | -49.76578 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef7be925-0560-3cf5-a133-7e553ef2e2d3 | -14.64654 | -48.405 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cabb63df-ec7f-33ce-ac4e-2bd016f54d78 | -10.3332 | -47.77981 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a5cbaec-9137-3dd0-842c-c11730e1fffe | -10.83881 | -47.88891 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bf40d75-40ab-35cc-a53c-7506ba38a3a4 | -11.08102 | -48.3361 | 2025-10-28 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5220817a-3164-37af-b477-44ed49a79d76 | -8.56528 | -47.01742 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 147da4b9-1f26-311c-ab2c-f471e0598f5a | -9.33816 | -49.28742 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89ff5d51-de26-380a-9098-13bafc304580 | -15.15957 | -46.58298 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea127f65-d5bd-3d3e-8cc9-e2df8b0abaa4 | -13.87503 | -48.49055 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4776f90-f0f1-300a-ac05-ac6a00d32320 | -10.59956 | -46.61718 | 2025-10-28 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c79713f-1a05-39f0-aa5c-f25f0d72e949 | -9.03804 | -46.93988 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6798facc-af8a-3509-ad11-5c54f45bec0b | -10.55906 | -49.82785 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d2d96d5-6d09-362a-8ce8-4475ced26ed8 | -10.96216 | -48.0509 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f41f828-df4d-35a7-8376-82160af4cb62 | -13.62723 | -47.03232 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76498200-8d4a-32d5-af4b-4e952f327307 | -13.22863 | -47.10804 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea5bafb9-7124-3dea-9715-817e174348c7 | -9.87263 | -47.46252 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 413ece6e-a99d-38f3-9ec5-9b2d5dc24913 | -9.29148 | -45.2203 | 2025-10-28 04:44:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4f9d48d-7ce0-3050-907a-f376bef6dd64 | -10.92667 | -50.26575 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a5aa88d-5177-3f55-b0fe-e025fbbc23d2 | -9.60931 | -47.80709 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed0523cf-4cbc-3cdf-a8bb-1c7aa194745f | -8.34658 | -48.16526 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6402a75c-4c8f-3948-8082-d03ad64a4550 | -9.5416 | -46.9551 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d44ade9-ff4b-36cd-99dd-bfaa7f7c8cda | -13.54514 | -49.58022 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89012190-6601-36f2-a4d8-a7fb5b774a87 | -10.87549 | -47.97881 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03aeda52-5fb6-3f33-b8a1-d21094e7eb7f | -11.28497 | -45.50772 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b4f84637-8ca7-3a19-8cf4-36d3ba93be6a | -12.81755 | -48.5623 | 2025-10-28 04:44:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b61886e6-93b2-3d90-8b04-765b9ba75e09 | -13.57222 | -48.52188 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a87f3e4-4d22-3e84-803a-e9411bdbcccd | -9.89307 | -50.04243 | 2025-10-28 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de7555f6-f443-3295-911c-92a9c95e5a1b | -10.5635 | -47.90076 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f410fce-e147-3e25-baa1-29937eb10d2b | -10.33501 | -47.76781 | 2025-10-28 04:44:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62cb420b-da1e-392e-9309-94a0a593b904 | -7.93598 | -55.01768 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4075e88-addd-3e06-a595-c6c3abbe10eb | -13.79975 | -48.65971 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 418ba162-dbcf-3af1-89ff-d9ef8717e87c | -11.10561 | -44.02088 | 2025-10-28 04:44:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4b6164a-9c17-32e1-9f97-fd923dba3e24 | -13.78078 | -48.49733 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9670c47-a654-33f2-804b-b7fe04131386 | -10.57961 | -49.80576 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0df25bc-971e-35a3-a491-8002d51bab01 | -13.22062 | -47.08319 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec6b87eb-8b96-335c-bebc-81da4cc0b95f | -9.34709 | -49.2961 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcd8fc9c-ac83-3d6d-af6b-ac33d9530ecf | -10.98938 | -50.35842 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a125658-2626-3e15-8054-448dc180cb3f | -13.6279 | -47.02756 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 05444fee-0276-334b-aa38-f2116214a6cd | -10.92445 | -50.27983 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4aeed5f-1c46-3af9-8895-ce95e866c26e | -13.26631 | -47.87433 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8680ffb-e509-3fc3-ad32-ca08524fc932 | -8.64106 | -44.77234 | 2025-10-28 04:44:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40fa9519-3031-3ec6-b04f-d37a7508bde4 | -9.60872 | -47.78701 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4d48e79-c405-32f2-9ac6-69506abc83f9 | -14.75915 | -44.95956 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 839b418a-ba33-3f12-9b0e-ddf1d883060d | -13.25049 | -47.72869 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 569c7e33-d517-38d1-a4a7-cf6e3b5b1aed | -12.08916 | -45.66539 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15aabe32-15ad-3dcc-b9e7-bc1b2d970761 | -13.23793 | -48.56671 | 2025-10-28 04:44:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a21caa88-8c07-30ae-afc3-f2927d577d39 | -14.24542 | -48.12061 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 176f065e-41c4-37cf-9d7a-a5e55cad9e5d | -15.15557 | -46.58241 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e0e9287-066e-3d52-b3ad-7ef2087f29de | -10.93464 | -48.04026 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a53ce4a-7490-3fd6-be7b-89ae272d85cf | -9.2713 | -45.57324 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0be1e25d-37c4-385d-bf74-e6a7a7acd945 | -13.63413 | -47.03862 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a91e31d7-bbf0-3777-a2ae-96bffd6b9028 | -17.98186 | -42.53365 | 2025-10-28 04:46:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8357c83d-9f9e-3bf9-924f-8cc1d52609cc | -17.4218 | -46.85977 | 2025-10-28 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8a369a7-9e28-3cb8-aff3-be33e0b05dd4 | -19.7966 | -44.49728 | 2025-10-28 04:46:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 06995f35-fce5-3a15-860b-ab7cfda96468 | -20.121 | -42.40016 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b625fcd8-1cc8-3823-a27d-6b3cacf57935 | -19.79482 | -44.49147 | 2025-10-28 04:46:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 61c6069d-2013-33c2-9d11-2f579c44e504 | -17.37634 | -45.35724 | 2025-10-28 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b0d99cd-a595-3c3a-ad37-763b302aa493 | -17.26347 | -45.29319 | 2025-10-28 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be1cfc2f-48f8-36c9-84b1-301b815c26f1 | -20.13925 | -42.41567 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1e024e7d-0fef-3bd0-a750-3b7af6e8e258 | -20.12383 | -42.3986 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f57bb2aa-7196-3a85-96fa-ed88097ce42f | -17.53665 | -44.61742 | 2025-10-28 04:46:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6714ed3-4478-33aa-8b9f-41b013c4a3f5 | -18.24845 | -44.19452 | 2025-10-28 04:46:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cf88ebe-7b32-3dd2-8298-1b607dec96d1 | -20.12137 | -42.39652 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 20015b50-1c9b-3e23-b175-6349c0dfba7e | -20.13668 | -42.41344 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e55aabb-1e05-3f38-8b13-b544108d3b08 | -20.12694 | -42.39762 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f18ac514-ba03-3bfd-9498-6cd242534fd7 | -19.79241 | -44.49059 | 2025-10-28 04:46:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a494f0f5-12d1-338f-9464-3c248246cef7 | -19.79728 | -44.49135 | 2025-10-28 04:46:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6dc06948-2dc2-3d65-9b74-32b008d71660 | -19.79418 | -44.49738 | 2025-10-28 04:46:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75cd60cd-f885-3453-ae5c-031e2663b27e | -17.62688 | -43.99586 | 2025-10-28 04:46:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa5165e8-fcd9-30e0-b104-a9731c4e90fd | -17.26849 | -45.2893 | 2025-10-28 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc83c672-1e2d-389f-90f6-19d7ca2acaa2 | -20.13963 | -42.41172 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 122ba6b2-34e8-3867-beb0-429390a5a8c6 | -18.78389 | -44.33922 | 2025-10-28 04:46:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 869160b5-f1fd-3cd0-9d17-3939b0a707aa | -20.1363 | -42.4171 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 897dbf6e-ed56-3bb9-ba59-17703ff4312e | -16.2695 | -47.75671 | 2025-10-28 04:46:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2281f5dc-6a14-373b-a3b0-491f2e7807d4 | -17.62329 | -43.99588 | 2025-10-28 04:46:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05bce1d3-b282-3cbe-8f1d-ba8d3248288e | -17.3237 | -46.09546 | 2025-10-28 04:46:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228e1349-c9ff-3426-8f29-f2cc55fb2fb3 | -20.12658 | -42.40113 | 2025-10-28 04:46:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 53ff2bdf-be6c-3e2f-9755-857467e931bf | -19.30075 | -44.37712 | 2025-10-28 04:46:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6da897fe-19b0-340d-8d83-ff5c9307abf3 | -20.14572 | -42.4075 | 2025-10-28 04:46:00 | NPP-375D | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b415c5a6-768c-36af-a809-f2b8fe849945 | -18.24663 | -44.1937 | 2025-10-28 04:46:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0275de80-1359-3f11-ab70-315741fdd4d0 | -17.69229 | -43.95962 | 2025-10-28 04:46:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 740e51b3-7de1-343f-981b-934a6f23bfe2 | -17.3808 | -45.35787 | 2025-10-28 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a8b7724-fefd-3deb-91f9-bc33dfaf4379 | -17.26795 | -45.29381 | 2025-10-28 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 371ebeac-3a35-3724-bcc8-88d053dc1710 | -29.95254 | -51.61552 | 2025-10-28 04:49:00 | NPP-375D | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 29d4ea02-408b-398d-83f7-b3b27431dc95 | -30.11417 | -52.08396 | 2025-10-28 04:49:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| f584ce28-3e7f-34d4-99f7-050307a807cb | -30.11775 | -52.08461 | 2025-10-28 04:49:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| aeac89a1-6868-3eda-93c0-57901029602f | -30.58663 | -50.57684 | 2025-10-28 04:49:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4f5eeb9d-b89f-3aad-8e40-98794ac42958 | -3.0158 | -45.3679 | 2025-10-28 04:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a73c38cd-5106-3e6c-93ef-23a4dd0338dc | -4.4632 | -43.2386 | 2025-10-28 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| a77af79b-c860-3d25-97cb-8b043410650f | -7.9461 | -45.5108 | 2025-10-28 04:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c1123379-fa56-3563-8506-084bd393cc5e | -7.9459 | -45.5335 | 2025-10-28 04:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README70.md)
