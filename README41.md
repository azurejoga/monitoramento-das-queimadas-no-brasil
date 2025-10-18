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
| 3e7f65a4-c8e5-301e-961b-cc9917fc7719 | -8.18355 | -47.0367 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 470289a4-dcfc-329f-88c3-819f20db9a0f | -9.75469 | -43.95441 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1337af4-436b-3701-bbfa-be6863ed7688 | -10.63431 | -42.30266 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6c7b6388-36e8-345a-8709-e1c12e7c86a7 | -9.25754 | -44.34739 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 854c4929-9412-33d1-8324-10c09b08a254 | -6.05666 | -43.40119 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c86c5eb1-6fca-3495-9d67-d6400b454be5 | -9.88445 | -49.11791 | 2025-10-18 04:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 098fe2b6-9b25-37d8-b9a8-40bc42064674 | -6.54772 | -43.91438 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15703901-7eaa-3577-9e4a-dc061a67d830 | -10.82508 | -43.93019 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566f4f46-4367-34a6-94b2-79ff996c287c | -7.35749 | -41.90239 | 2025-10-18 04:29:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 516c29bc-24c3-3273-8c8e-13576b95cdfe | -10.63381 | -42.30619 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2d929888-28c0-3c52-a28d-224a6e292e58 | -5.56028 | -46.36637 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cf842c6-fe04-350a-8571-1dc9648afc8b | -9.75345 | -43.96281 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7dc9aad-91bc-3bc4-90be-eb51901dc859 | -5.89221 | -43.91379 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fdc2f34-7ee3-3b7c-bc83-e6a016cdbf0b | -8.23089 | -43.31768 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 83857cc8-1c9a-3d78-92ad-cecbe3d54869 | -6.35283 | -45.75505 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b9b93a4-f0cd-3fc7-bf3e-eb1d5e64ef42 | -10.2944 | -44.02429 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d218425c-5f3b-31f8-9c4c-e6f39ae1cda7 | -10.48179 | -47.73392 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 371b4865-25a5-3af5-a284-d959e8ed59f0 | -10.49462 | -43.42066 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6619270-b876-3115-9038-68e5018a8222 | -8.54791 | -50.08052 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ed91c29-7681-38d1-896e-11ce7cf02f20 | -8.41843 | -44.72281 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68c27abe-222d-3918-bac6-11a834d963d1 | -7.48805 | -47.02916 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f488bfdc-6b16-3eea-9d4f-d207ae160996 | -10.49511 | -43.44366 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 34bd2507-d80f-3c6b-ba47-f72e36986071 | -7.17766 | -42.18116 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fe9e666-b1fd-3aa9-a5a1-9a100297ea24 | -6.42953 | -47.29971 | 2025-10-18 04:29:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8a592e3-62b7-3073-8f17-255d1b1bed62 | -10.2447 | -44.06005 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a95ccda9-d772-3d05-8e45-7890e948fcc4 | -10.25166 | -44.03716 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 853c9c7f-f0dd-3d8f-b307-5bf07268f97f | -6.23431 | -44.1551 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4216df50-9bb9-3b93-9889-0dc5c1e5cf7b | -7.46751 | -47.07244 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0378b77-a1e5-331b-b919-88ad3621d63b | -5.55696 | -46.36585 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c6c68d4-c671-3545-96e4-59863a32bfb7 | -3.85835 | -52.23166 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e56ec703-a81c-339c-8a4d-e821d3b9cd64 | -7.24509 | -49.51581 | 2025-10-18 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b81e21e-6207-3824-a33e-dba756007a84 | -10.35824 | -47.72116 | 2025-10-18 04:29:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973858be-8393-3e80-aaab-5e2519699586 | -10.1363 | -44.53498 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6af0f63b-23ab-3cfc-8d31-4f92c7bee7f3 | -7.0686 | -45.61488 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 853d9ecb-7496-34ba-b48b-59386c5a9ac8 | -8.19844 | -43.30831 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e36d80a3-1c9b-387c-8df4-69690b67821b | -5.86975 | -44.8468 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21a1b3e7-dcb1-308b-800d-e14393cc57c9 | -6.2272 | -44.14312 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd4e1288-a129-3b07-bfc6-9d3ca7b07761 | -8.94859 | -49.02134 | 2025-10-18 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a894b7d-af19-34fc-b26e-754c0212f1eb | -7.32143 | -48.46052 | 2025-10-18 04:29:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b631d2c6-d18b-3345-8891-8c827d4744d9 | -7.14443 | -46.42188 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b92f6529-36d2-352b-920e-8e523430893b | -8.35954 | -46.24567 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f61fd1da-cd4b-34a4-b931-ba0bc1e85d00 | -6.47051 | -44.13921 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57f2b871-e5d0-3948-981f-55a4a8b14e76 | -10.42888 | -44.90731 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddac6637-7f12-34a0-a67a-d4709e2c3e7e | -10.18581 | -44.53658 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dae0225c-c6f7-31f5-b376-4613274827c0 | -7.44454 | -44.74558 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d74c1bd2-87cc-357f-a12e-2ee3a57601b5 | -6.94549 | -39.60057 | 2025-10-18 04:29:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d0d316dc-615d-3e5f-8b69-dbbfcf466f6b | -8.60431 | -40.19086 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9538677c-dd2e-3489-9565-422d61028dd7 | -6.83408 | -42.42751 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b3106237-1973-34dc-8e2c-53e64ee47e60 | -8.16705 | -43.30119 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d4e9dde0-313e-3cb6-91f3-30aa817c4ce9 | -7.01291 | -41.83158 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 823df0cb-d250-3262-9756-24b28ae59d4e | -4.56906 | -46.94 | 2025-10-18 04:29:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccb3f8b0-f154-390b-a362-7c4fe5580755 | -10.63785 | -42.30679 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c9240716-f020-3181-86ff-c6d78ca8b33f | -5.24694 | -50.95719 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9a7025c-e35a-3996-8940-5e0a17607690 | -9.21273 | -46.8825 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 431b1194-1243-358c-a1a8-fd6bf43ca9fb | -7.82296 | -44.12255 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fdbb931-1b92-301e-8764-944b345ccdae | -9.66998 | -44.54857 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccf59b78-a4a8-3083-bbd1-cfadb8f59693 | -8.16146 | -47.02971 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e14de788-2ac7-3a66-9f64-6fafa1382fc7 | -10.4814 | -43.43238 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aaf3c6c0-8b85-3481-a557-ebf4b053c6b4 | -10.23828 | -44.05215 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33b9f614-d21b-333c-8aac-40ac724c5c13 | -9.13257 | -46.6193 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8825f4c-310b-3319-b04d-37a5d149dfbe | -6.32647 | -40.94528 | 2025-10-18 04:29:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1aa1c57-e07c-3fb2-b95a-ede1963af791 | -7.58262 | -44.98149 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00f05651-0a42-3163-a7fe-a8f95fe0e81e | -8.39227 | -46.23297 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f20493d-a57e-3cee-b689-663d6cfe0b20 | -8.69744 | -47.06536 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9063e8c5-9264-37b4-b2b9-2cf612ee1ad2 | -9.75407 | -43.9586 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01a1f9ed-e1d6-3821-b8c2-22f720f492c5 | -5.59727 | -45.98158 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1db75a01-355e-3a28-bc21-a24925a6e264 | -4.95148 | -47.82436 | 2025-10-18 04:29:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1725df6-4c68-3696-8381-3f187743f903 | -10.69075 | -44.55667 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 069fb5aa-acc0-3306-bb0d-4d979bb22e89 | -5.30046 | -45.47914 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d22ccf9-412b-39bb-bf57-44313b84a5d2 | -6.23549 | -44.65042 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 215be4fa-d50f-355d-8b2a-40c924e6bdea | -6.6157 | -43.61279 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 80c20301-5e1b-3f42-b76b-a424d93da0da | -7.01416 | -41.83017 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b6e2309-a16f-3177-a670-038eafdf3414 | -6.23488 | -44.15129 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d8c575f-fd95-3943-b23e-00721e0c1879 | -10.71331 | -44.55174 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14b6d8be-2f31-35af-98d6-2d1876257be6 | -9.25687 | -43.74879 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d108e2c-eb67-3164-a3ce-35853bfcf7a2 | -8.33831 | -49.97108 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5d99a29-2e84-339d-84ea-69e6edc68abe | -10.59552 | -47.99872 | 2025-10-18 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1190128-d70d-381e-8a94-95e851fdc790 | -6.6027 | -44.4408 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c2d9610-959a-33a6-b4c9-cc11c4ef7746 | -9.23924 | -44.37314 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c96e251-7d5f-3e48-be13-54ddbc928013 | -5.35565 | -45.03789 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19864c5e-08c6-3dd6-a110-094aefdce2a5 | -6.89727 | -45.45844 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3aa8d9c5-7ed3-301d-bb4a-1645344ecfaf | -6.23641 | -44.15233 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78bdebd5-0bcc-36d6-99c8-da5d9303162f | -5.7118 | -46.45464 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa30674f-cb9f-3b83-b540-5c583593e851 | -8.27196 | -48.00729 | 2025-10-18 04:29:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2828dd76-2cb4-35b7-90b8-d0583438e2d9 | -8.53842 | -49.59983 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef70924-a693-3a6a-97df-8aff0af977d9 | -6.58455 | -48.77417 | 2025-10-18 04:29:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50d4d6a9-48d9-36b2-9f82-561c59d004a7 | -5.78956 | -44.88998 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ae69c3d-8e0a-39e6-b30b-89579b7853f4 | -4.30261 | -48.06262 | 2025-10-18 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74225eec-420a-3551-b9a5-b2ecf1d8ab69 | -8.82115 | -49.68619 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d610a44-e56a-3f5a-b07a-c902afc07018 | -7.14111 | -46.42136 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4a4b017-5173-3c1c-be0b-d56d00fb83f5 | -4.96006 | -45.08585 | 2025-10-18 04:29:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee8128f6-0117-30bf-bcda-27ffee5e0688 | -8.53991 | -50.08353 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2af2cf-5e9d-3261-b98b-aff07cbc8bab | -10.63629 | -45.23307 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a224a62f-ecc1-3349-8b48-43920ba99ade | -7.71389 | -47.85147 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 970c0012-b31e-3e96-b082-e52249b1455f | -7.11343 | -44.78968 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5595a3c1-6394-318a-9692-2a8750c737fb | -8.86353 | -46.01078 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a165c65c-ea2e-366f-a236-d173562aadc4 | -8.35782 | -46.21312 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9b9c7ac-b263-3749-970c-47dc8cb24f58 | -7.7264 | -47.63777 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a092ef98-0005-3994-83b4-5e72297085c6 | -10.49022 | -43.42451 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31fe9ca3-1ed0-3f1d-bba7-537285ca2aaa | -8.36503 | -46.21068 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README42.md)
