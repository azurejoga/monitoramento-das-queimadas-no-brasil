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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb182ac4-bcda-3371-9ee8-8e20febcfe57 | -10.47386 | -44.85476 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d496301-f4eb-382e-8ffa-d4b56f1db712 | -10.57008 | -44.81424 | 2025-11-15 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c739fc31-8309-3ebc-8b08-c7699ac32147 | -11.17386 | -48.14587 | 2025-11-15 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db96fa01-667d-3f10-a8ce-56da357d44c4 | -11.70481 | -48.39764 | 2025-11-15 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e40e40c-52b9-3de5-a35f-f1d116763091 | -8.99722 | -44.18796 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f75a7668-633e-3ff9-8a90-0f0bc062350b | -12.39311 | -48.10616 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6df1e0b-88fc-34fa-9f2b-78d464615af1 | -9.72728 | -46.33754 | 2025-11-15 04:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a36679d3-c97d-3f96-b7db-15ca38e93cf4 | -13.48787 | -46.71837 | 2025-11-15 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79655ab6-fb73-3f53-ba63-919328e5d2fc | -12.15349 | -46.67514 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6660de5d-6bb6-3e27-a5ef-ac4191525333 | -11.84433 | -49.21176 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 24587500-856b-3eb7-83ef-cad9f8d5b039 | -10.70457 | -44.50026 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0dc11c0-cc2d-3046-a096-d6a58923a6b9 | -9.66709 | -43.0959 | 2025-11-15 04:06:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ebd5d36f-386c-3aca-a98e-7a1902ff0a14 | -13.73787 | -43.62858 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37d55378-3cff-3938-87a9-a1c43c2cc09e | -10.10827 | -40.89835 | 2025-11-15 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5b2195c-5576-3e05-a56a-776e74689464 | -13.35994 | -43.72013 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e56c697-54cc-3b3a-881b-91a83d971d08 | -8.71377 | -45.67563 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e78e4dac-b19a-3d53-8ed5-ca178f1676b8 | -13.74194 | -43.62535 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0c8494f-3906-33e6-a389-e09fafcebc81 | -9.05749 | -48.83034 | 2025-11-15 04:06:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0031eaad-6e06-3713-a54e-9046fc871257 | -12.67766 | -46.77407 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 5587dbb6-1803-3963-8f3c-a265b610479f | -13.35545 | -43.74728 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e25936c-d200-39d4-8165-ddfb089b763a | -10.04891 | -44.26361 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 254c5094-78f9-374c-9ee0-2346ce6ee66c | -10.70158 | -44.51798 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dad7267d-edd7-305f-85f2-4eb6381ec0bd | -10.80718 | -45.17178 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64519da5-ce84-3297-a40f-0d79f3ec00ae | -8.327 | -45.40902 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df062393-d602-3f29-8cc0-822061ecad72 | -7.53261 | -47.20104 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30ef2bf6-7322-31d4-a013-3e58d918f3f0 | -11.74608 | -45.33514 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5df09013-8b88-308d-9a14-912f618ac5d2 | -12.72491 | -44.55227 | 2025-11-15 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16be42bb-3eb9-3244-a839-c5a877911a25 | -8.15375 | -43.80878 | 2025-11-15 04:06:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 353450c3-332a-33d2-8b0f-0f708eb1b778 | -13.54706 | -43.7276 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5ab2cb6-fa56-3491-9891-7c9226aa87f2 | -7.06462 | -48.3228 | 2025-11-15 04:06:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44d3fc88-9c95-39eb-841e-9f4e3d8dce3f | -12.77103 | -46.95237 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 022f0bb9-ac31-3e2e-abf7-6327d0c06e9c | -10.62869 | -44.58757 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b81b3907-9de2-3a71-9633-40a239a838d7 | -10.09346 | -48.12136 | 2025-11-15 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b966258e-6096-3ad9-a9c6-8d466d4777fb | -11.66602 | -48.46495 | 2025-11-15 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 670da86e-b942-366b-bbe3-c435404f9774 | -13.48319 | -46.72127 | 2025-11-15 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a663539-a774-311e-a6ce-ad4f1d63ab16 | -10.33692 | -49.63911 | 2025-11-15 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57c7d07a-c2bf-3504-84a6-4c4434f4ec9f | -9.01062 | -44.17636 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b77c52-5724-3f50-990c-ba6b01c72fa1 | -12.43407 | -43.18502 | 2025-11-15 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 083406e1-506e-3cce-99b9-312cca35edae | -10.10547 | -47.52166 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9968e0ea-7c54-3d20-96bb-194baf2f757b | -9.7542 | -43.97504 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b466fc43-3b9d-3b75-b3e3-addeaa2674e3 | -12.81375 | -48.56186 | 2025-11-15 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e1a92d1-c219-3e51-bd62-edab7e2635a6 | -12.47987 | -43.73491 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17cc362a-5fb1-3e25-8d1a-72d20989c25d | -9.8266 | -49.77318 | 2025-11-15 04:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f105c6fb-22b5-384c-93b3-9be35173e4a2 | -9.75423 | -43.97316 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67802de8-3cae-3476-85b8-3df97b7c8fc9 | -10.88943 | -44.93649 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd7dd32a-9e15-3601-8673-ea04dfb05041 | -9.09428 | -47.78674 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edcad389-e5a2-3008-88eb-775f1f457aa8 | -9.81526 | -48.84308 | 2025-11-15 04:06:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 48471868-c697-3b64-bf8f-cb8d6dadedc5 | -7.21773 | -47.97411 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c9c4c9f-37c5-395f-904c-a79d71be7e26 | -9.85261 | -44.16553 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9519a8ea-2ce0-33ba-91ef-9424cf8706e7 | -12.65638 | -46.75099 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7f5d48d-5bc3-3803-ba82-698e1d3a0f77 | -10.88957 | -44.9393 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2e963f5-e31c-3aa8-8b58-7214cdf44000 | -12.47922 | -43.73884 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55d92989-3dac-327f-8ccb-e94eabda8106 | -10.66439 | -49.36419 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19a3a635-a2ec-3c74-838f-83aed73cedd9 | -11.74226 | -45.33454 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c6984a0-6e11-323d-9c4e-6df7d81e9f57 | -13.29186 | -44.23721 | 2025-11-15 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69bca20d-7a15-3109-b9f8-f3ed05876779 | -9.67812 | -37.0906 | 2025-11-15 04:06:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 181b3cd6-c131-3658-a09e-e004b58627df | -10.6957 | -44.50775 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e05ea325-ab1a-35e3-919f-154b2d0947cd | -8.86306 | -40.38355 | 2025-11-15 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0b386a9-e192-3a06-ac93-3dc50014dac0 | -11.84414 | -49.21997 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| dfad53e0-16ca-3295-84cf-d7a1472d3d46 | -10.10268 | -47.51876 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 508ff385-38cd-3566-9dbe-86734a0deeca | -9.81312 | -44.22741 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e2515a6-5698-30ea-a3ad-09ba4bf722dd | -12.56542 | -43.96114 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5229cf0-d75a-34af-bc43-399ab099111c | -9.66182 | -43.90223 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 264a78ec-2d23-374a-accd-d2f5dace39e5 | -12.47638 | -43.7343 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e46d6f01-251e-3b17-b919-5f15b473fd12 | -12.83807 | -46.43431 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5eb83f3-416f-316e-b61e-1beaf287324a | -9.12906 | -47.12502 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de8ffc8e-7352-3174-a94a-717a4f0b5aac | -12.7555 | -43.64701 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ada4fa52-7617-3210-a376-0d321c067820 | -7.76123 | -45.16305 | 2025-11-15 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6b8af54-f28b-36f7-b5a5-a4ac1740c5a0 | -10.42749 | -44.95002 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e061762-d622-31b2-852c-a62ef5534747 | -10.12643 | -43.89439 | 2025-11-15 04:06:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ffcf1d4-7598-345c-8254-b6d1864ef89b | -12.97395 | -48.83998 | 2025-11-15 04:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c3d6b8e-3e88-3784-86b2-2fa3f77febb2 | -9.5216 | -47.27112 | 2025-11-15 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21ab5b50-372e-363c-9ce6-8e334f75239b | -11.80698 | -48.07467 | 2025-11-15 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf2e84ed-6953-366f-b490-fc595adb18b9 | -11.16925 | -48.14503 | 2025-11-15 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e80d936d-85a5-3563-9c05-3f8602728296 | -10.66943 | -49.36518 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22ad61d3-5e3f-3b1c-b4dc-3b21fd7dda9b | -9.6302 | -45.18123 | 2025-11-15 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39b0b928-abb0-3760-a556-9777405d75b4 | -12.25947 | -44.91471 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d0b1093-bac5-3968-baa9-5573c435d893 | -8.15743 | -43.8094 | 2025-11-15 04:06:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b1530e3-0537-3413-8285-85ffcfd1fb36 | -12.47107 | -49.57492 | 2025-11-15 04:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0303c9b-fb0f-39d1-9058-30eaee3cc0c6 | -7.39086 | -48.65795 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38b22035-66b0-309a-a273-10c5e6aa7481 | -12.45915 | -43.75154 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ccea4292-55d7-393e-a6fa-c457ababf12e | -8.30112 | -41.38568 | 2025-11-15 04:06:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66788129-0361-3a3d-b530-c10585e79a9f | -10.69864 | -44.51285 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f583484-e255-3548-abc7-b75712d7557f | -11.85411 | -49.21369 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88796c58-9d80-31da-a302-6ce177ae7e0f | -11.71435 | -48.8707 | 2025-11-15 04:06:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3655aa9-1679-32d4-8c37-a191b3c68282 | -13.52589 | -43.41431 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f7f51cd-c7de-33c9-b469-23b3eed0fc50 | -10.17463 | -44.49706 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c4862b7-e306-3096-9b59-cfe9ca4194af | -10.0439 | -42.30397 | 2025-11-15 04:06:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81f636ea-5bf6-3eae-a19d-958af502d4a6 | -13.33206 | -43.18832 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24823eff-6a2d-355d-8ead-6b8e47c49491 | -8.58316 | -46.07278 | 2025-11-15 04:06:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e99023e7-8ce0-3950-a537-ebf389b00e56 | -9.12986 | -47.12056 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69f7924a-80fb-3b72-a273-98c22f45b64b | -12.67212 | -46.75769 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c0f77b-beb6-32a9-a0de-ebd676e2a7ff | -10.70602 | -44.5142 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16579708-dd0b-3ab8-afe5-157c2893203e | -12.36325 | -43.69886 | 2025-11-15 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b228d81a-b2a1-33b5-9bef-44cb0174cc49 | -12.69957 | -44.47927 | 2025-11-15 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4fed059-ae6e-3084-b835-cb0ba40430b0 | -10.70531 | -44.49585 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d08d7b3-2014-3a82-8268-70512c3930f5 | -10.88861 | -44.94115 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4fa393d-1673-38bc-a18e-daa1ec59b3fe | -13.48383 | -46.71763 | 2025-11-15 04:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e4ba9ef-50de-3fa5-b3c5-eb87b862b8fc | -11.79704 | -48.07769 | 2025-11-15 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2dfd32c-a8cd-31ff-acd3-ad765f194ff6 | -12.60053 | -48.3391 | 2025-11-15 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
