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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a05570ff-ff50-32dc-8d69-6bf6fbdb73de | -29.68804 | -51.09236 | 2026-03-12 04:19:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| cc0fcc70-8c17-32cf-82b1-f436f378ef52 | -8.06795 | -43.15287 | 2026-03-12 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85113830-977a-3856-b497-9833e7c51e1e | -9.16125 | -41.06176 | 2026-03-12 04:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3bd6fda6-cba1-3152-9b0d-b9b79d60572e | -8.06388 | -43.15221 | 2026-03-12 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 549e12a0-99bc-3f25-8ef1-6ff4c11fa2db | -9.15575 | -41.06631 | 2026-03-12 04:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 685d7e89-79ca-3f7d-a0a2-a3cce6e16c2f | -1.86434 | -54.68588 | 2026-03-12 04:34:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83bbdc68-6788-3d9a-a506-385786aac5cd | -9.15647 | -41.0611 | 2026-03-12 04:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d01abb57-b874-345d-96db-1a73fcbe2bc4 | -9.16197 | -41.05655 | 2026-03-12 04:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 56fbf684-6841-3f27-9fa3-ae5e4b92fa74 | -9.1517 | -41.06039 | 2026-03-12 04:34:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18048309-517b-3add-9aeb-ab42e3cab6df | -10.12324 | -36.13411 | 2026-03-12 04:36:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a03895b0-398c-3653-95ca-c4ad60805b4f | -12.01805 | -45.35192 | 2026-03-12 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e698e09e-1629-342a-9b2e-2ba50cb42e6c | -10.9683 | -44.61595 | 2026-03-12 04:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e57ee672-8a68-32cc-8482-ec9d386850ba | -10.91808 | -44.65194 | 2026-03-12 04:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 609765ee-64a6-3d23-a316-c48c6326e5bd | -12.97967 | -54.68389 | 2026-03-12 04:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7e7b14c-e093-37c7-bf25-88ddb667b514 | -12.98434 | -54.68103 | 2026-03-12 04:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 625abb2c-cdb6-3587-9ede-4742f05f58d7 | -10.12991 | -36.13494 | 2026-03-12 04:36:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f457cc1f-19bc-3983-b787-1b738bee745b | -8.8818 | -44.77878 | 2026-03-12 04:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6de50b66-c5bc-3e3b-a64f-7362c1618f55 | -12.07114 | -45.22454 | 2026-03-12 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9ede6b7-3ecd-3fa6-8aaf-1ef2cabce906 | -10.96697 | -44.61408 | 2026-03-12 04:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98a7bb89-1aab-39b0-be0f-dc5d5f67742c | -10.91878 | -44.64706 | 2026-03-12 04:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb17b48-8d8f-3f25-8eed-111a7999bb89 | -10.12693 | -36.13662 | 2026-03-12 04:36:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8b7b341f-5902-38ee-bb2c-2a8b5a76108e | -8.87932 | -44.78006 | 2026-03-12 04:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66f9c361-fbe4-35f9-9a70-57fa992300b3 | -12.51036 | -43.68098 | 2026-03-12 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 067f536e-2d13-333c-a606-ce71432c2eda | -12.9837 | -54.68463 | 2026-03-12 04:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6a2755f-0fa3-3843-ba05-25556ce2a6f9 | -12.0716 | -45.22234 | 2026-03-12 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2977e398-af48-3b26-b5a9-089ad08aede3 | -10.79882 | -37.15409 | 2026-03-12 04:36:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 75b91450-2b93-3da9-8209-daf8aa93af00 | -10.79821 | -37.15926 | 2026-03-12 04:36:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 15ffcdb0-893e-313c-a2b2-98f67d93d9f2 | -10.12397 | -36.12809 | 2026-03-12 04:36:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f36e6f63-be5b-3388-ab4f-34f5f5c096af | -13.4794 | -42.98808 | 2026-03-12 04:36:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3328f5a1-4b67-395a-8bd7-758ce722edc0 | -8.88113 | -44.78325 | 2026-03-12 04:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8660247a-2ac8-3bec-8a63-93828bbcb742 | -12.98031 | -54.68029 | 2026-03-12 04:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65f8a9d-c57a-373d-b548-5e4f0b897999 | -12.51089 | -43.67705 | 2026-03-12 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b33f7e-b92f-3493-a679-d9eb5f47f2cc | -12.07092 | -45.22702 | 2026-03-12 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2e58033-2def-3ccf-9e65-9d8a2e87b355 | -12.06713 | -45.22647 | 2026-03-12 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4780ef4b-9de0-36cf-aae4-b3be34bc73d3 | -10.12761 | -36.13072 | 2026-03-12 04:36:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7d531794-e481-3c2b-8595-eee45c6d4bfd | -10.13063 | -36.12909 | 2026-03-12 04:36:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 11862f84-31d1-325a-ab6b-437bc278004c | -16.9249 | -43.60089 | 2026-03-12 04:38:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d915dc95-2cd5-39a8-9264-2841e1d55cc1 | -15.53763 | -48.23883 | 2026-03-12 04:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c5707f1-2d3e-3bb0-a840-0ac611cd8b10 | -15.5348 | -48.2343 | 2026-03-12 04:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cabb6b51-1ac5-3213-b1b7-67bbf9559595 | -15.5382 | -48.23495 | 2026-03-12 04:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 727a4dd1-1a19-32d3-a6be-abc0f9ce0db0 | -29.68814 | -51.09644 | 2026-03-12 04:42:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 5ae6de6f-5f22-39ae-9905-f0751052933b | -29.68876 | -51.09203 | 2026-03-12 04:42:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| a90e717b-b2d3-391e-8b37-4a3e7c19d98b | 1.52497 | -60.17901 | 2026-03-12 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68785c7e-0eef-308c-9f81-e55ecadc5abf | 1.952 | -59.99333 | 2026-03-12 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1b59601-bb0d-3c66-9eeb-6cb86ef8a914 | -1.86416 | -54.68797 | 2026-03-12 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebfc5b8b-3c13-39b1-a922-c2d1a7aa0b86 | 1.73971 | -60.29199 | 2026-03-12 05:23:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7d92cab-cf87-3937-a835-89a6dd1594be | 0.77343 | -60.31344 | 2026-03-12 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dcd03bd-7e6a-3714-9c94-d61d09352c50 | -12.98148 | -54.68054 | 2026-03-12 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a41c4d3-eb63-3051-b25c-5d8804ab741c | -12.98618 | -54.68123 | 2026-03-12 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1156c32-ad80-35b0-9f50-49cd1f7632b2 | -10.99116 | -55.3624 | 2026-03-12 05:25:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82564a24-5e53-396a-8bd4-169054d2424f | -12.98552 | -54.68633 | 2026-03-12 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 846dc709-1ba1-30fe-9f23-3addf4e8f71b | -29.86908 | -54.849 | 2026-03-12 05:31:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| a0973179-5e05-3bcf-bab7-9b9931c73b79 | -9.15379 | -41.06504 | 2026-03-12 05:46:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8cd62e5e-16d6-31d1-8f96-1ae26f389dd9 | -9.15525 | -41.05556 | 2026-03-12 05:46:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3f3d78fe-c656-3ee8-8567-d8ada3787ad4 | -10.79961 | -37.1526 | 2026-03-12 05:46:00 | AQUA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 84b8a909-488f-3953-9543-667293ff073a | -11.35683 | -43.40216 | 2026-03-12 05:46:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ef24464-1623-3326-aa72-e8c1ce42a27a | 1.57105 | -60.30515 | 2026-03-12 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7582fbd7-1061-320a-84ce-db4563c42377 | 3.62995 | -60.85653 | 2026-03-12 05:53:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95af7e8f-fc2e-3992-8706-5de33166bac3 | 3.62622 | -60.85715 | 2026-03-12 05:53:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7314aac8-d122-31b4-882c-6a3116388b97 | 1.18257 | -60.83315 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28b782ac-35f8-3363-bfdd-02a93d098175 | 1.18575 | -60.833 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aec06a0-e91e-35f2-a67d-d0fbe697df25 | 1.18505 | -60.82862 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a63e746-c331-3909-a79b-e7333ecb25ea | 1.18434 | -60.82423 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86348b32-8c7b-3554-a113-5e2a951ccde0 | 1.18961 | -60.81888 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56fdb4d1-cb78-34dd-8cc8-8ff020a9d802 | 1.19417 | -60.80911 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d1c37f9-39bb-3b6b-89d0-3cdb8ff092ae | 1.18183 | -60.82878 | 2026-03-12 06:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1c68a85-bbde-39e4-a2f9-1f92e66de3cf | -9.49132 | -40.66439 | 2026-03-12 11:30:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 6051b93a-9fdb-3250-bd1c-d576a6cd1868 | -8.01175 | -37.20889 | 2026-03-12 11:30:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d98b0ab4-d21d-3087-a87c-c9f499afd2e0 | -9.36938 | -36.92344 | 2026-03-12 11:30:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 78e1c96d-37d3-341d-8717-e9d09a74e5e7 | -7.53124 | -36.75306 | 2026-03-12 11:30:00 | TERRA_M-M | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 1e7f0cd4-65c6-3e6b-94c6-47eddbdd646f | -12.68854 | -38.90564 | 2026-03-12 11:30:00 | TERRA_M-M | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 255a5768-319d-32e4-bee8-47d6cb3db2f0 | -10.80191 | -37.15362 | 2026-03-12 11:30:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 3f28cef8-1001-37f6-9a65-74ad7b03e13d | -12.069 | -45.2305 | 2026-03-12 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5002bacf-3b3f-31e7-aabc-ae65f9f8749a | -12.069 | -45.2305 | 2026-03-12 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 2dc616e7-321d-38c1-b118-d86f8ef64f61 | -12.069 | -45.2305 | 2026-03-12 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| bb32a46f-7567-3512-8abd-557d2e595a12 | -12.069 | -45.2305 | 2026-03-12 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 46b228d2-43ba-3a65-92b6-ee2724ffe8fc | -12.069 | -45.2305 | 2026-03-12 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 29789ef7-3941-3c89-add3-111b94159e8c | -12.069 | -45.2305 | 2026-03-12 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 8890ed55-c94c-31d1-8000-1974b4be8d81 | -12.069 | -45.2305 | 2026-03-12 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| f0e0add7-eab7-3e06-a67e-3bd825a10f27 | -12.069 | -45.2305 | 2026-03-12 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 6b4c797b-5fc0-3cf6-80de-a3842db76eba | -12.069 | -45.2305 | 2026-03-12 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e54cd31d-4ef9-31ac-895a-e7fec7468879 | -12.069 | -45.2305 | 2026-03-12 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e0777fa9-c074-32bc-aa8a-0896d94dcfbf | -12.7875 | -44.8406 | 2026-03-12 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |


