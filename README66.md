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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 107622b4-78a9-3ca3-95bc-48b46854c3dc | -9.05336 | -46.96362 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d0c62b-3401-389a-8e4b-3487924eaba8 | -11.19159 | -55.06684 | 2025-09-11 04:23:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 896fdfa6-185b-373f-98a7-ea10bd70a95f | -11.69913 | -48.2613 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72bfd242-d9b6-39db-bfee-04cfd330fcdc | -11.47569 | -43.63078 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61a04487-57a3-3915-83da-3153f84c11fa | -13.8522 | -47.33813 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a320d1db-2013-33be-ae0c-ebd1992de923 | -9.08427 | -49.85157 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b27317b2-8368-3d2b-acc3-8830bd271973 | -10.54069 | -51.50585 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 613545e2-221a-3d63-bf64-a4351d102f04 | -11.02199 | -45.05976 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f7f3eba4-df65-3073-a066-23fd7a154890 | -14.57042 | -48.76463 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c28a9d39-2af8-31aa-babb-69462a5f2220 | -10.57094 | -52.04137 | 2025-09-11 04:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f0c1737-ca23-3d79-bc40-a81eee336a9a | -9.0208 | -49.77374 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fdc1c5b-164b-3caa-bcc0-79aead621463 | -10.00124 | -51.72486 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f61f6b3a-9d6d-3b19-9aab-4919c09fe40c | -8.79567 | -48.09222 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca5c7b17-7947-3d69-b296-81fe30bd1222 | -11.71054 | -41.74178 | 2025-09-11 04:23:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72a95aa6-1341-30ee-b210-29a5d60ec226 | -9.06875 | -47.08494 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc29ac04-229d-39c7-98e1-9ef4145b6d4c | -9.2943 | -48.42048 | 2025-09-11 04:23:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f42e384c-32f9-3444-a5ef-bf1c3d9556b3 | -12.1319 | -44.85374 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18368214-3627-3bb7-9c55-6c5e49c0eec5 | -11.46988 | -43.6456 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7917f5d0-157a-33e4-980e-137c04133a24 | -9.12834 | -46.99485 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f06457f-43a7-3fb7-8ff9-998fc37ffeef | -9.01468 | -49.76249 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 00895eff-9490-3b62-8b36-a2aaf64ab74a | -10.74024 | -49.28262 | 2025-09-11 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5b63275-2cdf-32f0-8ff8-eed8d3ac2d09 | -9.76323 | -51.05858 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ee7615-fd2d-3ba8-9846-a1e6c37ef127 | -14.3015 | -45.03262 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57ca16f6-5e56-38c2-a698-4fe258c82e98 | -14.61689 | -48.84978 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf3184c6-f618-3f8e-96b9-4e8ad5b5c7cc | -11.4762 | -43.67407 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f3e4011-29d1-3f8a-80fc-69876a65e260 | -11.49138 | -43.67952 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5ea12b6-f864-38a1-94cf-61a451b12103 | -11.7285 | -50.62944 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 697e3db1-b70a-37b1-94e4-aa3328ea942e | -12.38091 | -54.16869 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 218b744c-05dd-3568-b65c-34b63db93330 | -11.99229 | -47.60263 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db8b167f-1f74-35c4-adb7-2ec370560052 | -10.06218 | -50.37617 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae073a28-2de1-30d2-960c-5ebc957e37aa | -9.96736 | -51.68768 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 946d2eb8-3eca-3d42-8a58-d2e80ba22e08 | -11.5006 | -43.66525 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| febfe613-c483-3aa5-b8dd-1a6ff210ee69 | -9.11992 | -46.98204 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d95f8dd1-b4a7-3bba-a05e-e278bf9307dc | -12.84892 | -47.96342 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17d43a51-36a5-3b57-80f5-962ffe2c6622 | -11.82435 | -46.7412 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58b874c6-8ac8-3b40-a5df-80a112000c1f | -10.3951 | -48.58415 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f46594e-bc1e-3d3c-a5d8-37048841914f | -13.65767 | -45.73169 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 723f3f90-99e5-3e55-b899-a7c1e61021b2 | -11.35736 | -46.51449 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a7fae4a-df5c-3a79-9598-288e2e07bf5d | -11.3656 | -46.55941 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dcdf565e-1d13-3d4e-810e-74f531254cff | -11.38614 | -45.58478 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe8085c-52ef-3db2-8e57-34cf62eab173 | -11.9895 | -47.59832 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fedc40c-df06-3c34-b1ba-404b5614e00b | -10.31763 | -48.80095 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a452b5cc-c72b-3aab-b766-bc01be9700a0 | -11.15766 | -48.34762 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04a1987b-a7b0-3c57-a15a-ded026c60a00 | -11.02478 | -45.06384 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 80e18073-d2af-376a-ab77-bfc6d728ffc0 | -13.84313 | -47.35158 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 716520a6-e4fb-3373-9833-7a84e32b4a41 | -13.90674 | -47.98965 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 222679e5-51b9-3b91-8059-07019be92a91 | -14.12265 | -44.31736 | 2025-09-11 04:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e30fdee3-afc0-38fb-9432-a013ea3b4db5 | -11.81594 | -46.75077 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0280b8d9-89f5-32cf-96e9-d1f8abe6b031 | -9.3055 | -46.76675 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14034432-0f25-3f35-962e-49afeda7fdb0 | -11.38946 | -45.58532 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1cbc335-cc73-30c0-816f-d7fa825f3259 | -9.07917 | -49.80952 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5d54cd3-8734-3688-b4fc-defe71eff89c | -13.23131 | -40.95179 | 2025-09-11 04:23:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9280ec8-2c7c-38dd-997f-f35c59156c64 | -12.92968 | -54.80693 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7459ca4c-b194-3f78-a65a-7cfb4a478286 | -11.96787 | -46.65132 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cafe752b-d10a-340d-a20e-8ef0291a5166 | -11.56748 | -43.23818 | 2025-09-11 04:23:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c31e674f-3341-3153-abf9-941118a5b18d | -10.54648 | -51.5227 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8bbfaf5-e477-3904-82cf-34b4f8ad75c5 | -9.66271 | -43.52131 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba529a7f-7af1-38d7-a994-89f8b2b00a1a | -13.97291 | -48.24506 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db43b2a6-4b32-3753-8a07-a64dc844d371 | -9.05451 | -50.49878 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63093573-579c-3996-b087-f3b0c90d347d | -12.12406 | -44.85988 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7fa9b1b-d032-3fc0-83b0-f72c5b563333 | -10.1355 | -47.89098 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9974db3e-e24f-3ba2-9989-a26596d46eb5 | -11.50553 | -50.38603 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e2a277-af57-3d37-be6e-9e5c09cbd682 | -11.45951 | -43.59676 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13a050e0-1118-37d5-b96c-5abea255cc3c | -14.57319 | -48.76932 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69d46453-0689-3e0e-b3ad-e340a65ead99 | -14.13702 | -45.40178 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 471e0059-34eb-36a5-9a67-932b5b67fccd | -10.55215 | -49.89103 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b0867ce-6d92-3a35-84df-e44d551b0e49 | -11.97358 | -51.11054 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f260d2c-55e4-3a1e-ac9f-f61f15a5a764 | -11.18304 | -48.36754 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 040bbd5a-b682-3986-a4c8-b9a23b537808 | -12.93535 | -54.80484 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f49bf91-dcc0-3e29-b23b-4eec12042dff | -11.48377 | -43.64772 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9bb4f7b-44ea-3164-86af-286c1286f222 | -10.17469 | -46.18325 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f6011bc-e700-3589-bc61-5e785de49a29 | -9.08586 | -49.81254 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9929d63-561e-3cef-b811-ce057ca2f9b7 | -12.96268 | -54.75734 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a380bfb-b1d0-3a2b-bb6d-97526a73ed55 | -12.13695 | -44.8434 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88a43db5-5d87-3ed7-a20b-50b371ceecc6 | -12.12968 | -44.86815 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f388937-41ab-396a-b7b7-26c6eb8b54a6 | -11.48734 | -43.6828 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11049f43-50ed-3555-9474-84d9fc447857 | -12.38475 | -54.17548 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 961e8eec-05d9-302c-9d57-f4964025d439 | -12.92879 | -54.75592 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4220278f-67eb-3c83-b4d6-c9a6944ace28 | -12.25172 | -47.32006 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca75f4a-50ad-3f57-a372-3133b7d51fb9 | -9.90366 | -49.90966 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00ffabcb-82bc-3bb2-a245-0a2e1f7549b6 | -11.47745 | -43.61921 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02d48c91-a0a6-3cfa-9a50-0d160ea0b016 | -9.90506 | -49.9251 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26c6383f-714d-3385-92c3-401e10e03f30 | -11.46355 | -43.61707 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97b93399-b585-3ef4-92ce-beabedc0bd53 | -13.44788 | -43.48513 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cef55a7-8149-3ebc-873d-1b2792a980ab | -9.98568 | -49.06052 | 2025-09-11 04:23:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4d12b5b-32c9-3775-85eb-1c76e36e1c88 | -12.31191 | -42.10449 | 2025-09-11 04:23:00 | NPP-375D | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7777abe6-5277-3d2c-8a12-df6c03f184af | -9.09761 | -49.81452 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38dec183-e9c7-3b1b-9e31-754b27aa65cb | -12.40412 | -46.63166 | 2025-09-11 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a748101f-0967-3013-bef4-560486933ed8 | -11.74317 | -48.12432 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4429dc82-41cf-3ffa-a7ce-dd7d4460d3e0 | -14.39186 | -47.31055 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 990b8e9f-ebb9-3d55-8fb4-16b39d5d4d88 | -9.07336 | -50.4868 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8761b8fe-619e-3219-b28a-1cda9a227f10 | -12.55815 | -46.93559 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5ba5a6e-207b-3129-a8c1-a35433e0910d | -11.26221 | -51.12657 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d9fd115-c033-3505-a146-abb887362f95 | -13.58801 | -47.67287 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce462544-87a8-30c3-b041-61b2df41dbbe | -11.99814 | -47.58835 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca5195a7-0dfb-3b7d-b495-68994ffe8bc6 | -12.97757 | -46.7219 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0de8e190-9cf3-3e6a-9377-1c7d4533019a | -9.67786 | -47.5317 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52940e13-b159-3fc3-82ad-457d7c0896d3 | -12.83276 | -52.94313 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37329e51-e780-3f36-8b2b-e3cd7b4d3c00 | -13.13355 | -54.92615 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2e9d58-525a-3b22-bb47-e3a5f3d950d1 | -12.47496 | -47.49271 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README67.md)
