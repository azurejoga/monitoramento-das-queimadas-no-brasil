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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cb19046-1e78-35a7-a587-5f02aafd94d7 | -6.8211 | -59.2651 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 423.2 |
| f3a466de-6946-3213-b0f1-0c89de06c769 | -8.0321 | -43.1257 | 2025-08-01 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 77f56591-eb1f-3513-a167-ed4998b9946c | -6.7295 | -59.153 | 2025-08-01 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| ab2ab3d7-bd39-3c3b-a47c-aa315f16e4c9 | -6.748 | -59.1523 | 2025-08-01 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| c6c21628-0535-3e13-9653-08ec8b8cb238 | -6.7294 | -59.1723 | 2025-08-01 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8f9e59a2-5e5a-3b8e-87a7-91da91089943 | -6.656 | -59.0981 | 2025-08-01 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8681eb17-b877-3d05-b0cc-855d61348718 | -8.051 | -43.1237 | 2025-08-01 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 74c72651-daed-3341-acb0-99769b30644e | -8.0513 | -43.1001 | 2025-08-01 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 50b58eee-c802-353a-b802-30114cb36b4b | -6.7478 | -59.1716 | 2025-08-01 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a0921cd7-c103-3d60-8f8b-d657e1d17d5d | -6.656 | -59.0981 | 2025-08-01 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 339f9916-be6b-39c4-bacb-ab08d0459fce | -6.7294 | -59.1723 | 2025-08-01 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| c8bd6d35-504f-3db7-abda-ce936de03e98 | -9.45745 | -57.83028 | 2025-08-01 06:50:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e6044fe3-35a6-3bf2-86f3-b37aaa44afad | -6.81255 | -59.25566 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 2f4b67e5-ea9a-3097-95d2-d4d976549f8f | -6.82047 | -59.26708 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 5ae03951-f5f4-324f-b351-199015380566 | -9.4556 | -57.84369 | 2025-08-01 06:50:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 5c696d7c-ba67-37e7-8af7-2eb3c799ea28 | -6.83128 | -59.25834 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4a6c42f3-8b2b-3909-b7b5-28861695db87 | -6.7326 | -59.16609 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 965ab4bb-42cf-30fe-8fa5-3eb4e3d6548c | -6.61788 | -59.96233 | 2025-08-01 06:50:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 444b2a93-291d-34c0-88c6-5d9e90ea1176 | -6.62421 | -59.98228 | 2025-08-01 06:50:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 87d65dbb-d506-30e9-ac99-f93a5775d88d | -6.82191 | -59.25703 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.3 |
| d151be12-7b50-3576-921a-d72b1d4caa0a | -6.72683 | -59.16887 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eec7c3e0-f23d-3d77-aef8-36040d121abd | -7.32331 | -59.61897 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9d2b5230-976c-3314-9d58-a749562e0824 | -6.72534 | -59.17897 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 5fa42f7b-5aef-37fb-b789-381cb9dedfc9 | -6.742 | -59.16745 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d6be901d-5d18-326d-bc00-ff8bff0280a8 | -6.82983 | -59.26844 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 95a8376b-47a6-3751-9d9f-f1e20c1212eb | -6.64426 | -59.09959 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6b4f1aad-1b77-3416-a5b6-b480dd0ce434 | -6.74345 | -59.15731 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9490e863-261f-3a5a-9f33-55974bbb4401 | -10.1066 | -58.22395 | 2025-08-01 06:50:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c41aacc2-d7ce-3c1a-93ef-4375de25dcda | -6.81112 | -59.26568 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a065ffed-d54a-3a3f-8d8f-433e4701e654 | -6.61652 | -59.97167 | 2025-08-01 06:50:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 545cc1fc-d890-308c-97c1-abebafa8da2b | -6.64577 | -59.08932 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2cedc304-5db2-3ee7-9116-d1e16908b3e0 | -6.62557 | -59.97296 | 2025-08-01 06:50:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 6a6ca90a-9672-3ec8-ba58-6885e8f4a8fa | -6.73115 | -59.17622 | 2025-08-01 06:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2248e4a0-83f2-3964-906d-87ef9f5f109f | -12.04038 | -62.14079 | 2025-08-01 06:52:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 043aab7c-84bd-32f4-9073-2ce30cde4b58 | -6.8212 | -59.2458 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 70ef9011-77eb-319c-b5e3-e823666c60e4 | -6.748 | -59.1523 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9d19b220-f1de-3ff1-845c-57e93f5ed3f1 | -6.7294 | -59.1723 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 6bbbd400-d6eb-3978-bf92-cc51b70750e7 | -6.7295 | -59.153 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5b318405-b5c6-3511-8258-e49facf816bd | -6.8026 | -59.2658 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 5585ca4e-b4b1-33fd-893b-b6f84d8e6713 | -6.7478 | -59.1716 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| be8b166c-dbe8-3c21-b7f9-f60f9e46dc5f | -10.0815 | -46.7441 | 2025-08-01 07:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| fb4b17d9-4e2f-3f3c-9950-2b792fa50c13 | -10.0812 | -46.7665 | 2025-08-01 07:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d574b259-c02b-3fa0-91d6-abde5157372c | -6.7293 | -59.1916 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 26745807-2129-3ceb-90fc-ba7e0ff69c08 | -6.8395 | -59.2643 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 237d17c6-9930-3220-aa25-59fce929d430 | -6.8211 | -59.2651 | 2025-08-01 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| db3f1f32-ff21-357f-9467-ee79b8dfc284 | -6.7293 | -59.1916 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 812fd483-78f8-3190-bc6b-da32d8492051 | -6.8211 | -59.2651 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c1464783-5105-3a72-a408-adf1d2436c4e | -6.656 | -59.0981 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ead43bca-5e43-3d18-829b-493cb12dfcd4 | -6.7478 | -59.1716 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| fca25181-3f6b-3edd-bc17-acc19207083c | -6.7295 | -59.153 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 65e48549-1155-3954-8663-b276a9a531f7 | -10.0812 | -46.7665 | 2025-08-01 07:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| db26e57b-ee07-338c-a939-fe91d810daf3 | -6.8397 | -59.245 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 08e8f4e5-2091-3046-be88-a16583d5f3db | -10.0815 | -46.7441 | 2025-08-01 07:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 24190b1b-a14a-3569-8ceb-b7b884bd2b7e | -6.7294 | -59.1723 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 312259f8-1444-33e0-8d8d-d66fc4104bdc | -6.8395 | -59.2643 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 52ce774b-ccfe-3922-86b8-774c38b96bd7 | -6.748 | -59.1523 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 30feb0ad-f3bd-302f-b1a0-0bf7714a1eb1 | -6.8212 | -59.2458 | 2025-08-01 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 09a8ca8c-ba58-3201-aa7e-1900d80e695e | -8.0321 | -43.1257 | 2025-08-01 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 80e739a2-82bd-36cb-b0b1-c7f5bbddfdde | -6.748 | -59.1523 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5ac83d51-7bc8-356e-a7c7-b97e5b5cc63c | -6.7295 | -59.153 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8719a35f-f373-38b8-a30a-7ef099c43519 | -6.7294 | -59.1723 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 7e3b36ad-a805-39aa-a32f-66e1d8e1ecd3 | -6.8394 | -59.2836 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 22bdecbd-885d-363a-8415-af02871182c0 | -6.8212 | -59.2458 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 875b6581-4fc2-316f-ac9f-1158cc6197d6 | -8.0513 | -43.1001 | 2025-08-01 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 763404cd-b76d-3938-ad90-bb3203ee14b0 | -6.8395 | -59.2643 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| a94b222e-a7e5-3d30-918e-8fecc910ba2e | -8.051 | -43.1237 | 2025-08-01 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| d31c26d2-784c-3795-aa14-854f183e0cfd | -10.0815 | -46.7441 | 2025-08-01 07:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a84da134-d439-3756-b4b3-8e60781a1cd4 | -6.7478 | -59.1716 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 2e664593-1dbd-39c5-8199-7026d8686890 | -6.821 | -59.2844 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 709095f7-2867-37df-840a-3c55a46009ad | -6.8211 | -59.2651 | 2025-08-01 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 234.5 |
| dd4b983e-cf0c-3871-a046-e595c070aa19 | -6.7295 | -59.153 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9afc6ec3-b8ac-380d-93bd-5665ac397e26 | -6.7478 | -59.1716 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| b30894f8-34e4-31f1-8c44-10677b82bff5 | -8.051 | -43.1237 | 2025-08-01 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| e2b44736-cb81-3fb4-8735-3a749ea5b92c | -6.8211 | -59.2651 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 4676aa25-e137-3b3e-8f98-2bbc86cd2c4f | -8.0321 | -43.1257 | 2025-08-01 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 2c4ad0a9-a990-3ebb-9418-a72d2b71d71c | -10.0812 | -46.7665 | 2025-08-01 07:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 80c30a40-1e35-346d-b24d-56d444dc36e3 | -6.748 | -59.1523 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ffc96237-e7c2-3536-8c11-069c633441a3 | -6.8395 | -59.2643 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 43625b33-1d1a-3985-b596-9990beb82328 | -10.0815 | -46.7441 | 2025-08-01 07:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f887e17a-9b7c-3758-96ce-4a3512698606 | -8.0324 | -43.1022 | 2025-08-01 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| d9338450-b4e9-37f1-99d4-8ad7e269188d | -8.0513 | -43.1001 | 2025-08-01 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 1a459055-4a43-3ac8-a9eb-4dc289d2cbb2 | -6.8212 | -59.2458 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b02a8db7-ea23-3aac-9ad4-740d21475400 | -6.7293 | -59.1916 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4c5766ed-844a-3b94-846f-1bcec50fbb1a | -6.7294 | -59.1723 | 2025-08-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.5 |
| b1cf13e6-d051-30c7-8d5c-c123903c2d89 | -8.0321 | -43.1257 | 2025-08-01 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| e472a25b-3da4-3698-9f97-b68f01df3194 | -6.748 | -59.1523 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3b2e4f41-3411-3813-ab22-1e3ba7879ab0 | -8.051 | -43.1237 | 2025-08-01 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 635fc4a4-45a6-3a43-8053-fa5506c1d588 | -6.7295 | -59.153 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1977b67a-52f2-396c-b22a-7a7a6aa5bf5e | -8.0513 | -43.1001 | 2025-08-01 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| ba53d8c5-c318-3447-b1bb-2668cec3b108 | -6.7293 | -59.1916 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7a435a3c-906d-3ae2-b8d3-67ac70e66802 | -6.8395 | -59.2643 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ebf721f8-c6e6-3903-8b7b-49f574e1f3ac | -6.7294 | -59.1723 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 015d8e4c-afa6-3751-b5e3-0744b89aca11 | -6.7478 | -59.1716 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| ebeb83c9-1985-342c-9654-ae30586d58b8 | -6.8212 | -59.2458 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1d3c7878-47af-3ca4-927e-3b013b47456b | -6.8211 | -59.2651 | 2025-08-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 02d4d4ee-79bc-38c5-9f39-b828c5d702d7 | -8.0321 | -43.1257 | 2025-08-01 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 82f7f7f7-575e-3a8c-8f86-96af6478ae68 | -6.8211 | -59.2651 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 275.0 |
| 2e6cb7c1-fa09-3dff-9779-7975650b9b90 | -6.8212 | -59.2458 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d3282c3b-0fa2-3f2c-ae13-cf5e3b6844f8 | -6.7294 | -59.1723 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 79ff8d63-5ff3-3d03-93dd-434882cd6362 | -6.748 | -59.1523 | 2025-08-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |


[Clique aqui para ver as próximas entradas](README28.md)
