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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33b51571-5254-37a1-ba07-eb92b7ca6a16 | -5.59973 | -48.08165 | 2025-11-02 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c825f6e0-8561-3b9e-b3be-c9807349447b | -7.40144 | -40.06952 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 87579de1-50cf-3628-be2a-c5543b2b2119 | -6.16501 | -41.63637 | 2025-11-02 04:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b5d2464c-d90b-3ba8-a35f-09e30d872ca3 | -9.27553 | -40.53112 | 2025-11-02 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 485d367c-99e9-3466-8140-2752e570e9fe | -10.99422 | -54.0036 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29bee123-39a9-332e-9f63-aa47f14f3109 | -10.73965 | -46.21719 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aff4096c-5c05-3358-acf5-4f2909403ff7 | -7.06164 | -46.7547 | 2025-11-02 04:21:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1daad77c-280b-3795-b679-a3d12c545509 | -13.01949 | -44.10519 | 2025-11-02 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9829ff0e-f451-31d9-b146-58affd3ed66b | -7.33053 | -41.23611 | 2025-11-02 04:21:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8929a958-ddc4-367b-86f3-b1b3f1bba1e9 | -7.18387 | -41.93899 | 2025-11-02 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 322725b9-0eb6-3e25-8dca-f1df85b6e2e4 | -9.06856 | -48.83241 | 2025-11-02 04:21:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 485303da-2326-3b48-9624-5bf2c01165e0 | -10.99485 | -54.00198 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf19f3d5-af81-3acc-9cfc-317175ab140c | -12.77947 | -43.44895 | 2025-11-02 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99da9134-0246-3361-90e8-5397780d0a14 | -9.44699 | -43.20168 | 2025-11-02 04:21:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90d1d24b-438d-3b38-8d23-990b12d3ac21 | -5.12507 | -45.81884 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82f1c351-6bdc-3ea1-ada2-8be3d32f11bd | -7.17741 | -41.93387 | 2025-11-02 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 441f64f9-3b35-3576-abb6-2c098f24b6ce | -10.72737 | -44.05968 | 2025-11-02 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eadd858-28d7-3551-bc6d-c1399f765025 | -10.62988 | -44.67841 | 2025-11-02 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7dc0132f-c8fe-3ff3-a0a8-8862de98dc96 | -7.17681 | -41.93785 | 2025-11-02 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2a481242-59bf-3da4-b8ad-e4253df00556 | -5.53897 | -48.12688 | 2025-11-02 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac2351a9-c262-3157-ae43-cd5a8ec9d753 | -9.27562 | -40.52965 | 2025-11-02 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1ab707c-77c6-3844-bc07-3a1acd986511 | -10.56985 | -44.53861 | 2025-11-02 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b8fb194-4dbc-3c5b-abca-d58f2c353d0b | -7.69757 | -43.10222 | 2025-11-02 04:21:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67c9925c-6ab0-3e36-9431-1468f54b3f5a | -7.18094 | -41.93443 | 2025-11-02 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1fa27a4c-ca9f-3296-85a0-ba9e44871bed | -10.73241 | -46.24131 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b38477b-7c84-3aaf-8bb6-5974aec90c9b | -8.12704 | -42.21592 | 2025-11-02 04:21:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c83b079d-2458-3ad4-b741-943b22dc2d74 | -5.34915 | -45.37518 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56b570a9-5139-34a9-9783-8e612ca31d58 | -5.34971 | -45.37167 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9d2897f-ea20-37bb-95a2-3aaac11356cf | -10.74016 | -46.23534 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9da3df14-928b-3839-871f-7b37dc55725a | -5.27168 | -47.22791 | 2025-11-02 04:21:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 513aef10-3768-36d2-8cf5-8ceee4de67cd | -10.62099 | -52.1894 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9596600-8f24-32e2-a010-225e5e38fbfc | -10.55375 | -44.53243 | 2025-11-02 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9bb5c2c-78ce-3bef-a662-c9dbfb1afcf2 | -7.26282 | -42.47972 | 2025-11-02 04:21:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1576be83-3312-32e8-b4cb-6f0b55000db6 | -7.84289 | -42.91246 | 2025-11-02 04:21:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 765e4507-2376-36c0-9aa1-558dbc029321 | -13.24012 | -40.94952 | 2025-11-02 04:21:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5012f741-ed41-3b18-89bb-01514bc588e5 | -7.10874 | -38.30569 | 2025-11-02 04:21:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b4471fc9-b713-3cb4-b7b4-64884348b7a0 | -13.12268 | -42.30648 | 2025-11-02 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce55a972-199d-3eec-a51e-f73655fc3333 | -7.00846 | -38.8116 | 2025-11-02 04:21:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ed3c1a15-1095-3b9b-9744-ac0b57c988ee | -9.16784 | -40.97124 | 2025-11-02 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fa1a06e9-0003-3981-92c9-b0e1a61428d3 | -13.02347 | -44.10194 | 2025-11-02 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbb158ed-bb48-3aa2-b77f-29075772b7b1 | -11.3663 | -54.31422 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b739cba-9bed-3cbe-af43-f89858a97af2 | -9.31215 | -41.06935 | 2025-11-02 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 33b5ff4f-9ca5-3b61-893c-837e310013c2 | -10.63151 | -52.18201 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05f96b4b-3e88-3ebf-b14a-5b60d06ccc4f | -13.03144 | -41.04729 | 2025-11-02 04:21:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 81d9c7a1-4ab3-3719-bab7-71fa831d6786 | -7.03433 | -41.46447 | 2025-11-02 04:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b419da95-4797-3060-9e0a-658a38142092 | -9.85369 | -44.15316 | 2025-11-02 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f9cabc0-45d7-3784-8068-d768b6c41cc2 | -10.73348 | -46.25595 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 065de4e4-8e18-373d-b8ac-9448401d317a | -10.78277 | -56.81961 | 2025-11-02 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db5c107d-2e25-3da1-a2e8-f05d782b1dc0 | -5.31217 | -44.42005 | 2025-11-02 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e077b75-2b10-3bdc-b8e1-fe22db132cea | -10.73522 | -46.22369 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 524f6946-6eb9-35c1-a6ea-ef1cc68d8eb1 | -10.99366 | -54.00657 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bb86fda-398d-348a-8796-477bd31ce25a | -10.73185 | -46.24484 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c09fd85b-971c-347b-908a-da11bf964223 | -6.89398 | -46.20648 | 2025-11-02 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 412e4418-d742-3919-80e8-67add8a6eebd | -10.99377 | -54.00792 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0773dcdf-b46a-37cf-9826-a138fe132e96 | -7.88351 | -39.10015 | 2025-11-02 04:21:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 69a9b228-17f0-335a-9334-d7f526d54312 | -5.31601 | -44.41712 | 2025-11-02 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d77c50f-f7e3-36de-afce-42dc0d70ef58 | -5.12392 | -45.82604 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d84d65e-29a0-3f10-88f2-759623e5cdce | -11.08231 | -54.25038 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51badb33-3a6d-3ba1-8f1d-3078827e4cb4 | -8.15706 | -44.48535 | 2025-11-02 04:21:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf9eec87-f636-3ad7-ab3a-0786e3acb581 | -10.97365 | -54.25047 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65b14855-38b9-3840-81bb-49e43690ed7e | -10.73736 | -46.25296 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c770aa13-46f5-3138-93c1-329317172cfe | -6.22737 | -46.45873 | 2025-11-02 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab802f43-3d04-3c2a-a1a8-88f6dff7a812 | -7.19732 | -44.26982 | 2025-11-02 04:21:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 951a9e6f-fc2d-3259-b6e6-142fe5f4ae88 | -5.11994 | -45.95941 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a03d8c5-3e2e-31c0-8976-e31be2285739 | -3.78404 | -55.44353 | 2025-11-02 04:21:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15a2d6be-a537-3ab6-9410-e10146ef429e | -8.47365 | -40.95561 | 2025-11-02 04:21:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3c11d74-08c2-3ab1-b65d-2ad6a49eb4e2 | -11.37038 | -54.31019 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6bb10813-19fd-3111-aa73-3859a5e2fc14 | -9.31196 | -41.0715 | 2025-11-02 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d05f1994-0976-346c-90c9-749eaf702037 | -7.39739 | -42.47229 | 2025-11-02 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4b7c510-9f59-35a3-8eb0-29503f7301ba | -10.6218 | -52.18488 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0030d061-3e05-361c-9c10-e4bdac358ce5 | -10.50876 | -51.8787 | 2025-11-02 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f95fd940-b17a-3d0f-becd-443900a56145 | -5.48292 | -44.98145 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d978514-0cd2-3aed-a097-0719784165b5 | -11.14361 | -46.54431 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd2a03ff-87ac-39b2-b0dd-d84a140ba514 | -10.30326 | -53.77356 | 2025-11-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aaf72dc-bbf3-3cd0-8f25-cbed20cd18dd | -10.99922 | -54.00456 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1036852e-3c9a-3572-a0d9-546dac7e975c | -10.73573 | -46.24185 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a93dee08-1d38-3167-9e19-4f9449dc1e52 | -11.57128 | -47.07948 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79a9beac-7335-352c-ab49-6a0d354337ed | -10.9954 | -53.99899 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ab2f273-2a40-3650-a9c2-0314c21cbbbe | -12.6738 | -44.44542 | 2025-11-02 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c95ca30a-dc3a-306c-b45f-46ed026047b1 | -10.74409 | -46.21068 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec99cec8-f470-3761-bd0c-b6b2bf97825a | -9.13707 | -51.305 | 2025-11-02 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 064ad220-be49-310f-bbc6-fe5ce21dcef2 | -7.01443 | -42.15247 | 2025-11-02 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 933b9f77-e3ff-3207-aba2-d2540f9db463 | -10.42263 | -44.8975 | 2025-11-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7be96317-610b-3871-ba88-38bf2639f48c | -5.24463 | -46.14425 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3e0063a-a466-32e1-b6cd-a778e04d4ce3 | -11.57463 | -47.08002 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc9e3168-99ce-3e1b-8df8-6b65f9905e6f | -10.74021 | -46.21367 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 423ac6b7-fe43-3d4b-8cab-cf1e574048ca | -10.63071 | -52.18653 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c084224-1441-3765-b75d-5fefb4608c44 | -9.78288 | -43.85899 | 2025-11-02 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ea5ee3e-88b1-3a5a-a561-04da96e91075 | -10.50823 | -51.87996 | 2025-11-02 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 809f68aa-54b9-3572-8fe9-714d962dd56f | -10.55312 | -44.91138 | 2025-11-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65861e47-1d98-35bf-8031-225c51059280 | -5.60201 | -48.08099 | 2025-11-02 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d15782f3-a0e8-30b9-a01f-74be2a18a765 | -3.79489 | -53.88221 | 2025-11-02 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 382a39b4-a77a-3a1e-9a20-0e64ea09fd84 | -5.34582 | -45.37464 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 992f2019-4b58-3d0b-a9f5-f7df19d6f080 | -11.3653 | -54.30922 | 2025-11-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 061f5c99-94b9-30a9-a46d-75c4fa17c223 | -10.30273 | -53.77641 | 2025-11-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19f5441f-8891-387b-8a3d-b9c37b900442 | -11.02781 | -44.03514 | 2025-11-02 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2624efe1-9ea5-33ca-8896-b9ff0bd561f2 | -5.12845 | -45.81939 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c8ff054-8568-3aa1-9982-62c4edcb567a | -9.13778 | -51.30087 | 2025-11-02 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0380ebab-19b5-397f-8782-f52bfcdbcb3f | -5.48623 | -44.98196 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3af17ef-e11b-3553-b306-428d01fd5176 | -10.74011 | -46.25703 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
