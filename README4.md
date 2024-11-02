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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ac0b3c9-2824-3d3f-b715-882190becbe1 | -21.66189 | -42.10871 | 2024-11-02 00:50:00 | TERRA_M-M | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a4460908-d288-3ac6-8879-cf8c37de837d | -21.65242 | -42.11018 | 2024-11-02 00:50:00 | TERRA_M-M | APERIBÉ | RIO DE JANEIRO | Brasil | 3300159 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| f9262548-c61b-38e7-bd68-c064ee97e663 | -20.94642 | -46.99469 | 2024-11-02 00:50:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ce602d60-5e33-3997-923b-a744145b4962 | -19.9517 | -49.55697 | 2024-11-02 00:50:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1d3892af-dbfa-34f0-9e30-14c0cdfdebcc | -10.66611 | -51.83626 | 2024-11-02 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 77bad4ea-b6e1-3994-ae28-16f8041b1ccb | -10.66418 | -51.82116 | 2024-11-02 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8cf1ecec-4821-3af8-809b-3daf7649f42e | -10.85444 | -51.87651 | 2024-11-02 00:52:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a32154c5-9f93-302a-8aa8-2fa06510af28 | -8.73801 | -40.58131 | 2024-11-02 00:52:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 6d946baa-459a-35c3-9d4a-df892bccb95c | -8.73462 | -40.56029 | 2024-11-02 00:52:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 2861fba7-de4e-343a-af5c-8212dcfb8333 | -8.60999 | -40.5052 | 2024-11-02 00:52:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| f199872f-5aa1-3ced-853a-3f797730f506 | -9.63373 | -40.59069 | 2024-11-02 00:52:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| adeccf00-2280-342f-bc29-cf03e2750292 | -9.63181 | -40.5844 | 2024-11-02 00:52:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| df0857b3-4c8b-34f1-b5ca-f97663b407dd | -12.33746 | -43.67352 | 2024-11-02 00:52:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6602dd2f-20fc-3969-8371-168722f874c8 | -13.22352 | -43.97548 | 2024-11-02 00:52:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 15a6d314-e858-33f5-a0cb-a3135b3fccc3 | -11.05074 | -45.371 | 2024-11-02 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4e294fca-cfbd-39ee-8b06-f656622f01d1 | -7.96397 | -47.18795 | 2024-11-02 00:52:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fce6a93f-dc52-3cc4-8644-a55b06b0d4da | -7.96271 | -47.17905 | 2024-11-02 00:52:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 18c0a629-74f5-37dc-8669-767c24d17e2b | -8.90464 | -48.53211 | 2024-11-02 00:52:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 057a9ab7-72ab-39e6-8770-1bd57e6827da | -9.85882 | -48.37445 | 2024-11-02 00:52:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 10036046-f8d8-32d5-a6ea-dd21cba77444 | -9.85753 | -48.36508 | 2024-11-02 00:52:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 146ad6c9-ee93-3c9d-8d7e-a6c40dd8500d | -11.58047 | -49.36219 | 2024-11-02 00:52:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d8f88dcb-8934-306d-8d6b-1b511cf7f454 | -12.6695 | -49.98418 | 2024-11-02 00:52:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dfcbb0e6-115b-3af9-b26d-a782d7b246f3 | -12.57141 | -50.01588 | 2024-11-02 00:52:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2fb514ca-c4f3-32a7-b9dc-515dc74fd2b7 | -3.45688 | -50.16716 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 44df93b1-f37b-37e8-958c-3e535850400c | -3.45569 | -50.29375 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dae5bd36-c0ae-37da-8716-cec72946674f | -3.45556 | -50.15767 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d19cbd53-a095-38e7-bec8-fbeeaddd5669 | -3.45035 | -50.18741 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 71be5646-0cb0-31c7-a10f-8615831aad5b | -3.44918 | -50.38315 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 974bad5d-5017-3d12-800e-a97740f06294 | -3.44903 | -50.17791 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 6202f68e-2c0d-3628-a5b0-ccf65dc9cb62 | -3.44641 | -50.15897 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36769e57-0ea3-3d21-8fb0-727bc94823b0 | -3.43201 | -50.32644 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4c48fb1b-97f4-3ff2-beb2-8e23f50d27d2 | -3.4307 | -50.2484 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bbef1913-7095-317d-80bc-235b3b2c6c6d | -3.41756 | -50.28931 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 04629031-3ef8-336d-8837-033f54e4bea1 | -3.41625 | -50.27972 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bc5c958c-93b1-3902-9126-60e5cf953fb3 | -3.40836 | -50.29057 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 798b6682-c63d-3f40-b2cf-ffdd7e6399c3 | -3.37927 | -50.27126 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ce2f5d8d-b441-3cf6-b196-abed57063374 | -3.37794 | -50.26167 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 493e49d6-f0bc-3568-a5ad-ff869263af5a | -3.37008 | -50.27253 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f65f3642-735f-3a6e-9635-7bf57c95821b | -3.36875 | -50.26292 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| b3766e00-8abc-3357-a376-82dab681663c | -3.36473 | -50.16656 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a89d4b30-4ccd-3ebf-9552-256356b423b0 | -3.36342 | -50.15716 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 944275c3-6f42-343c-a083-dc800bafb764 | -3.34907 | -50.25597 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 67e18856-e43f-37e2-8d8a-4387b20a4fdb | -3.33988 | -50.25723 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 233b80e4-9bcd-3f96-bed1-cb413d6e85c0 | -3.33858 | -50.24774 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 94971823-1f69-3f57-b96d-78f24c741edd | -3.29836 | -50.02243 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0af60a2f-8c3f-3aa0-973a-22af79774eef | -3.29096 | -50.2316 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b502728d-ca69-3ead-9398-db206724ca56 | -3.2831 | -50.24232 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e9dc7dcf-2f46-3623-93fb-eb73302bc43b | -3.28179 | -50.23288 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e4a84554-1012-3343-9a42-691952978d50 | -3.26875 | -50.34173 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a0395981-d649-332d-9e63-416a7605b7d8 | -3.26743 | -50.33215 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 34636d52-736a-3e79-b1da-473a4c2fd91a | -3.25689 | -50.18789 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a41eb48a-1675-3c48-8192-7ff12c604190 | -3.25687 | -50.05358 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0f1e7c1-8dd1-34dc-a97c-692764891be5 | -3.25557 | -50.04422 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 32c6d571-49b2-3239-9e12-09c04905a883 | -3.24774 | -50.18917 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f9dba7f8-d5b8-3a59-943c-d58648afa55a | -3.24647 | -50.04548 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5204c458-195c-3b3b-906c-72bdd7b14d97 | -3.18204 | -50.58747 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8dd78541-ad71-3e32-bca0-393a667a8989 | -3.18071 | -50.57765 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| acc69707-d6c5-3ce4-a434-2e37d999c4e1 | -3.17273 | -50.58877 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6e1af8a7-6f2f-39b6-ab32-e4a5a23b1b9d | -3.14109 | -50.35572 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| df179d2b-ebe8-3679-9696-ee7bc7f54b9f | -3.0937 | -50.47669 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 86b4a74a-0ba8-3e0c-b4fb-887f16738df1 | -3.06865 | -50.22639 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 682db7f9-e9a1-35d5-9f35-18bdcd25b126 | -3.06858 | -50.49997 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 951c69e7-3bc6-3baf-a554-885af2a0bed9 | -3.06243 | -50.50676 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 399551cb-d262-3785-81d6-b31c4c163afd | -4.15323 | -50.74942 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6277e24-3033-30a6-a41f-6384a4d119ce | -4.14374 | -50.75077 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| cb5310bd-2120-36cf-a1d9-f5d81c37f4ce | -4.10028 | -50.75259 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 246ca416-d329-39c5-9df1-871317f79956 | -4.38346 | -49.67429 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d7577b6e-e166-37e5-95c7-f97319afb9cc | -3.91684 | -50.43665 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 41411c69-0ed9-3696-b202-5242a85ecb4f | -3.85253 | -50.43181 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0d0bbdcf-6a36-30fb-a5dc-f97ee239c1a6 | -3.77212 | -50.37898 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1f3fee0a-fd71-3667-8d1e-528debbcef22 | -3.71376 | -50.55378 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| beca2446-9e13-36f8-9c83-61fdf2bdbe79 | -3.71237 | -50.5438 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b973c1f3-27e4-34ed-9561-1588bce07acf | -3.70329 | -50.15297 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ab4c8e7b-bb8b-39b6-94a1-26ffdcbe9de8 | -3.70303 | -50.54509 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1be0286-2891-3dec-8913-54467f54aeba | -3.69411 | -50.15423 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| b9665621-e447-337b-9a38-c88a02bce57a | -3.69281 | -50.14473 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 701cde8f-73b5-350a-b533-6f95e941d297 | -3.69122 | -50.59744 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cec56cae-b349-3822-befc-0c1bd61d16b0 | -3.6255 | -50.18962 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 819cd21e-9f4d-3c4d-8245-4a2e9ddb4235 | -3.62418 | -50.18007 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5ff3077c-d2a5-31be-b7f1-2479bb1d61d0 | -4.80933 | -49.49035 | 2024-11-02 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 81247237-fd15-37bf-8d70-4f32fb0239c7 | -4.80807 | -49.48117 | 2024-11-02 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8b692060-71b4-3a53-bbd5-3d3001b69211 | -4.80031 | -49.49165 | 2024-11-02 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 216a3a8d-9e8f-3b07-8e6a-b41b447b7f88 | -4.79905 | -49.48242 | 2024-11-02 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d4178289-8ae0-31e7-aacf-c1070d3441ff | -4.71568 | -49.613 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfc27d06-8c19-377b-a2a4-5e15f172f20e | -4.71442 | -49.60376 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 80674865-a487-3338-a386-65416e0593cc | -4.70663 | -49.61428 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e72c69ea-5a32-36b6-ab31-0e005e5e1a46 | -4.70536 | -49.60502 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c8020255-811f-3e95-a147-631302d8a22d | -4.48412 | -50.13231 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ec054c7f-92b8-39aa-bc9a-e633be557f2d | -4.48278 | -50.12266 | 2024-11-02 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e30c1724-4fb7-37e4-8f2a-bb1bb4820248 | -4.06839 | -49.26282 | 2024-11-02 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f78512c8-4e77-3c39-970d-185b35e08229 | -4.05946 | -49.26407 | 2024-11-02 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d39bd086-8149-34f2-8d0f-c63f7c0254bd | -5.50443 | -49.58739 | 2024-11-02 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ebfd843a-ae19-3d0c-943d-696ef6d73159 | -5.2384 | -49.93368 | 2024-11-02 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ee6f5681-1a12-3fb5-bf33-100479cf2971 | -5.17379 | -49.86065 | 2024-11-02 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8e821a36-b88c-35d4-9821-0dbd2729cea8 | -6.84995 | -49.9976 | 2024-11-02 00:54:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9477772-1e10-3a63-9272-74ee1fa9af04 | 0.13865 | -50.48163 | 2024-11-02 00:54:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6ef17c39-ce04-3094-9f27-3a5acb6b22e3 | -0.16167 | -51.38864 | 2024-11-02 00:54:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aa3e9b60-b7c4-3bae-97d3-88555020cb0a | -1.63873 | -50.47581 | 2024-11-02 00:54:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8af4eaa2-1247-3a45-9d4b-607f17349860 | -1.55151 | -51.62368 | 2024-11-02 00:54:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 465bf32e-1f49-3d58-9964-3d7ced877172 | -2.26028 | -50.4424 | 2024-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |


[Clique aqui para ver as próximas entradas](README5.md)
