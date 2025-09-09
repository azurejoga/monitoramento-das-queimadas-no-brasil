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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef3601bc-a8d8-305d-867d-a4183e1e763a | -11.13827 | -48.35669 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f50158b-79c2-3f34-94a9-d526bb049ec0 | -11.02661 | -46.03708 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c40b3a4-159d-35ec-890b-03ad118dfdf8 | -10.98267 | -45.098 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 9e8bf2ce-94a8-3b65-b8a9-65607f5e4825 | -12.61768 | -56.96783 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f05d6157-703e-310f-9ae3-b08e81710030 | -7.7116 | -44.75034 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63a66770-c8ab-3d5a-ae8b-ff736c7af317 | -9.65318 | -48.02114 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4e13679-ee8c-3320-8eb8-e63542e36ce7 | -12.62167 | -56.98133 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec1f08c9-7b1e-3bb8-88c0-c975a42f318f | -5.89681 | -53.84196 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 955fa85f-a8ff-3567-ba17-4c448df4eef7 | -9.46192 | -60.51268 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12a55d1f-7ef2-35a4-aeed-29f9e2780bbf | -14.32483 | -47.31862 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 37236f8f-b40f-3f80-a3db-bbcb1bfac5ce | -10.28748 | -48.81972 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c8468e6-708d-387e-8d78-0d98c75b5fed | -8.60568 | -54.69309 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd42136-fa6d-31c0-a3c0-82183c2848a7 | -12.86504 | -47.97128 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b328ddb8-62ad-3538-b14f-ecbc3fde6eac | -8.02072 | -45.5195 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b4792e5-eef9-3b5e-b6fd-2cb816edcdba | -12.61419 | -56.96945 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c4d09ae-4d73-3371-8540-138a11e1ad11 | -13.84351 | -46.2337 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f84fc278-1444-339b-aa49-dc798cef8792 | -8.03022 | -45.50441 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df364c51-9af1-3e81-a6d5-421e4623104f | -11.67166 | -46.88286 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a58af2b-f3a9-3701-a8da-8675444b97d0 | -14.30285 | -49.41822 | 2025-09-09 04:34:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf6746e7-ccd6-3061-a5e2-63faf5ea835d | -13.65295 | -46.97118 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35b3c1aa-42ce-31a8-ac4c-9e4b86f0ef62 | -7.65649 | -48.00211 | 2025-09-09 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c30eb3b8-9b00-3eaf-96bc-4589b25a4113 | -10.98578 | -45.10315 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fdfe7aa-fa20-3582-827b-6886030b8734 | -12.55163 | -49.13437 | 2025-09-09 04:34:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ee55914-cf05-3bae-94d5-ba6f8bfb8e30 | -11.1188 | -52.03447 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 116605a2-77c4-3a98-bfc9-b7b161d126fb | -13.27823 | -43.74038 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcbc8965-1679-31c9-9591-50ff99f3cca4 | -9.09511 | -45.71645 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57d7b790-0400-3a36-862b-af5d9ac410c4 | -8.05604 | -48.64694 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e747e701-9140-3bd2-8f04-5c13726e7532 | -11.79128 | -62.74346 | 2025-09-09 04:34:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d1aa7be-5599-3c7d-8c1b-ca8974d9c76d | -12.19479 | -53.88532 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2cb1deca-8b81-393e-a3f2-e1d48ca94bbb | -9.81955 | -46.02876 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb07519c-3fe9-3adf-a7b8-2e4f9feaf2c7 | -12.96088 | -54.76004 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2219876-a182-313b-9a3c-857bf15eb4a9 | -12.82805 | -47.98801 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c05b61ab-0c7a-3ba2-b4cb-fec8e48af899 | -9.45733 | -46.43707 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb724a38-8807-3641-83ac-506dd95fea2f | -9.0888 | -46.97504 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f5db53c-b251-323d-a5e2-b99da3159716 | -11.29148 | -46.49606 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cfb2d3e-0e7e-3611-bd2e-0d5927d643a4 | -8.05437 | -48.63605 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38e181ca-22a2-3c8a-a211-dd0f8a179031 | -8.04194 | -45.54741 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e70744b-97c8-3537-b70c-ae0ec05deacf | -13.50776 | -50.80946 | 2025-09-09 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e27597a2-1927-3653-81d3-288dd2e7d6a5 | -10.97389 | -45.10595 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 50619951-3b9e-39d5-9316-de7364cb704d | -9.13628 | -60.52453 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f7f1351-2721-35eb-82a6-bee47653f72e | -12.60733 | -56.97128 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f243e02c-4231-323f-ae57-791941700941 | -9.74243 | -43.51729 | 2025-09-09 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 766df5f0-44a5-3d21-9283-24f082244551 | -12.19118 | -53.92335 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4aba563-bc9e-3f41-a47b-ab14d52bb90c | -11.03115 | -45.93157 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 687347ba-9b2c-3e91-ba2a-06f61c2e659a | -10.81191 | -48.29009 | 2025-09-09 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 922ab107-64a0-35c0-a432-2bf2d07a94e9 | -12.62616 | -56.97467 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 243a4e04-7dac-3b89-a246-0ac576b0766c | -8.85707 | -47.25074 | 2025-09-09 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a196f75-9d59-35cf-9f95-c58e1db612d3 | -7.78583 | -46.08672 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 54ea032a-2522-3e99-837b-033d75c823ab | -11.39647 | -43.5475 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 822ddd50-fff7-3c7b-a4f2-afc54ac0832c | -10.07315 | -48.09807 | 2025-09-09 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f114d7d5-b677-3a35-a3cc-363ee02bd80e | -9.55882 | -48.67099 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fd35b75-9049-34fd-b97e-c69484000a24 | -11.6543 | -46.88052 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ecab175-aab9-3733-88b4-06bb8e4ca3f2 | -14.17187 | -48.98868 | 2025-09-09 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e54b9f8d-fb65-3a63-a4c6-73849d6b7150 | -10.14918 | -46.19493 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8791790-4bd1-3130-971f-2f758ff59dbd | -11.42321 | -50.33017 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0ebfe91-539b-327f-9e6d-4c1a99933b6c | -11.84018 | -46.77929 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43cc04f2-d83b-33c2-b5c0-4a9827699185 | -12.60639 | -56.97639 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c809c2d-df0d-387a-90e7-2d1903bbca5e | -12.20079 | -53.89663 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d5d41171-3e70-394f-a957-59f1165dc88c | -10.98203 | -45.10257 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 328ef032-e3f7-3e68-9001-12b709bc935f | -12.85324 | -47.98098 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa6e3e19-2a59-3450-ad4b-e7b78fa04917 | -10.58206 | -52.02959 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2068685e-87a6-39ba-a027-45ba8cce1ac9 | -7.66884 | -50.29612 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48a3419c-1d41-3b13-b044-c22e942cc384 | -10.35912 | -46.44506 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5926a540-be60-396c-a119-c246ea999129 | -9.79172 | -46.23941 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e355fdf-a9c4-34f7-b29f-e80c377f78ea | -9.72578 | -46.79438 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9b0d179-8eff-35db-9d93-ad53ab1636ca | -13.74674 | -46.89743 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d8ca0e-c7ad-36ed-aceb-61c34d4a3f9b | -12.84652 | -47.97976 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2cae978-d9ff-3db2-b856-72eab37c19ab | -5.50385 | -60.13401 | 2025-09-09 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 389eb72a-2572-3ffb-a8eb-eaf57d4b9c0f | -9.45712 | -60.51494 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b6a277b-0524-3b2b-af6c-76ec62d09b33 | -8.37646 | -45.01088 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e69f7b1-dc85-33b3-9232-404a82badb91 | -10.15888 | -46.208 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7963e46b-72b3-3b48-89ef-93bd878f226a | -11.46714 | -49.26088 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6a421b8-ea26-3330-9a49-0287b8335d1e | -14.33872 | -47.30759 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b173d0f-a890-3703-8817-75da40d22f9f | -7.71098 | -44.75451 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db021376-061c-3819-9a3a-6226dbbf9a33 | -13.7965 | -46.27577 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bbda7ef-c15d-3c23-a3d7-0f719483dede | -11.21047 | -55.0004 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6d806a18-ca87-35cf-9831-392decca6cef | -12.4624 | -48.03203 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d73ed4b7-d720-33e8-acf7-30290bb9a279 | -12.94876 | -54.75778 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ec9923e5-f1f7-36fb-8752-485a56a631bb | -10.5899 | -52.02671 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b0d04d85-2cf6-3ff1-ac4f-b2a57cd23a3d | -10.97053 | -45.12143 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 976e750c-ba0d-3315-891f-7589571afa2a | -12.55548 | -49.13138 | 2025-09-09 04:34:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69358380-480b-3f88-be81-d3e8fc293944 | -9.7082 | -57.79221 | 2025-09-09 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52fa51a-f3d0-3385-9ec8-688d1de78605 | -11.437 | -43.63797 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fc63413-18f6-3959-95c5-5e79e17d63c6 | -12.18792 | -53.87898 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a770f5-c99d-3768-bf3a-ea543229754e | -11.37781 | -43.52904 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02445e46-68db-3acb-8be5-9ba3c504efa2 | -7.25666 | -44.81687 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1689e80d-25a0-31b5-9f86-23b6b436b18c | -11.51505 | -50.30877 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eeaece63-9b52-320f-ad94-812faadeab42 | -12.18546 | -53.88648 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1936e78e-eb05-32ed-bc1e-66a1b683a97a | -11.63296 | -52.24018 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2dc4851-c8ef-3bfc-b469-e28ed61c6488 | -10.08032 | -48.09563 | 2025-09-09 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 201fdc7e-0be7-3833-9fe8-30c44652ee1d | -9.48879 | -55.97904 | 2025-09-09 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9459c38-5cc1-31fc-a186-79876a8bb28f | -9.43653 | -60.52119 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94f7503b-7d4b-3924-be02-10b7b89dca0c | -9.29769 | -60.85843 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61829ddd-155e-3df8-bb08-2030281efc54 | -7.14823 | -46.05756 | 2025-09-09 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6da8181c-4d8f-32ef-af00-363e93ac9b69 | -8.91628 | -47.88317 | 2025-09-09 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fc7ed07-56d8-301a-9a68-063650dda22b | -7.78641 | -46.08292 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad8430b3-2759-32a1-a903-99369247d43d | -11.84758 | -50.70102 | 2025-09-09 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66d33a05-95a8-388c-b4bd-2dcad2ac6ceb | -13.84335 | -46.23656 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d951fc8e-d63c-38ee-8a6e-aa080f277107 | -10.41381 | -59.60373 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a92101e1-d171-3e12-8d25-2bf2444b281a | -9.82308 | -46.0293 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README39.md)
