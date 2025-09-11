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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7734a5fd-2410-3fc8-a50c-00281e386e2b | -20.04088 | -42.73203 | 2025-09-11 03:57:00 | NOAA-21 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 491a3660-f5ee-36df-b970-176c5806e8ba | -15.89825 | -48.18185 | 2025-09-11 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ae9fb87-6d9d-3bb8-b87c-b34c2939cbba | -13.32893 | -46.37539 | 2025-09-11 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab4522a3-5c2b-3017-953b-00194b446ac2 | -19.98991 | -47.6277 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 72ffb369-8459-3dfa-a6b4-d745aec850fe | -17.7343 | -39.52351 | 2025-09-11 03:57:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0dc1c89-0eec-3fe8-951b-8eddfe779a96 | -13.6585 | -45.72048 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4e14040-a61b-350a-8cb8-3736dd5439e1 | -15.68046 | -47.02294 | 2025-09-11 03:57:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45064468-71fd-3aee-8b36-403c7710d0a7 | -19.66394 | -45.8527 | 2025-09-11 03:57:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa238011-ac0a-3a16-a24a-9de20434ab96 | -15.09637 | -48.04519 | 2025-09-11 03:57:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0326786d-7aab-3cc8-9423-bda774d1b0c4 | -14.3743 | -47.30052 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bcc6dae-32e5-3282-a17a-ff926ed37eb6 | -14.91823 | -47.30761 | 2025-09-11 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0d7767a-7d60-34e3-8d02-060089490bcc | -14.30901 | -54.74747 | 2025-09-11 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77bcfe3b-f911-36d3-9f14-2a75f965340e | -18.57363 | -47.42061 | 2025-09-11 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 689f0061-858e-3f07-abc4-ba26786b8cf9 | -19.38073 | -41.81672 | 2025-09-11 03:57:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1b4059ee-5ba0-3186-9adf-83bda364d2c9 | -14.41254 | -47.32074 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9d8a647-1dc2-34a4-a97a-e20d2ad2512e | -15.12431 | -52.4026 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f75b0c8c-ad57-37e6-9ff0-3547b312d762 | -15.20415 | -44.04521 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a8423ff-9784-3749-acc3-d49018e93077 | -20.0808 | -46.66275 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4b0dcfd-0783-39a3-b5f4-167a04a83889 | -14.14353 | -45.41674 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0395fd2f-1943-3ca7-88f7-24da4f37fb1a | -19.66857 | -45.84873 | 2025-09-11 03:57:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45317b2f-6b74-3503-9133-376001f0aa5a | -20.00652 | -47.63133 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2061517-f712-3bbf-84d4-0d0597b9542f | -20.23926 | -43.579 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 080c5087-c0fd-358f-9d50-c6d4508daefb | -17.27056 | -46.08565 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7ad6408-1874-3306-83f0-f5a0365a28e1 | -19.80595 | -47.16328 | 2025-09-11 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1018f9f0-5fb5-37e4-b918-489d47f87a5f | -17.55172 | -44.54427 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35226153-2918-399b-90ea-9b7f773976f3 | -19.92332 | -46.16966 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e235b3c9-e90d-37ee-b4a4-df09b6ff8925 | -17.73666 | -44.49947 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 784afb00-7e34-3928-82fc-222147494264 | -18.34406 | -44.35769 | 2025-09-11 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce95ede1-b74f-32df-a20b-971b11654a49 | -16.00689 | -44.8682 | 2025-09-11 03:57:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afa9bd7e-5ace-32e2-a1d0-d5301cdf23b0 | -19.30355 | -43.26088 | 2025-09-11 03:57:00 | NOAA-21 | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7dc35f99-c2a3-3541-aea2-86eedee7c798 | -20.16758 | -45.46563 | 2025-09-11 03:57:00 | NOAA-21 | JAPARAÍBA | MINAS GERAIS | Brasil | 3135308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 827a71e6-3ab9-395e-b6b7-48750d66fd53 | -17.7692 | -44.44099 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9e52ac4-191d-3b12-a09f-9a221436ea3e | -18.28046 | -39.6979 | 2025-09-11 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aaed6272-3be1-3345-ac71-f63122bf525d | -20.12694 | -47.68652 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4dc43bd-05da-38de-8c32-76b4a142e366 | -15.4819 | -49.35958 | 2025-09-11 03:57:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4406bd6-fb0d-3271-a1a3-49b0c635d3f0 | -20.00912 | -44.23506 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7cda8213-0ad6-3c7d-b312-b4c76914a439 | -15.14308 | -48.60656 | 2025-09-11 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bb2f7cc-8d67-3716-9e49-1ea1ab889911 | -18.35539 | -49.32727 | 2025-09-11 03:57:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0ec7adb-383d-3801-8175-48544bfa46e1 | -17.55325 | -44.53546 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c863335a-9803-3306-87a2-02b00933b08d | -14.1198 | -44.32017 | 2025-09-11 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a3728f17-d5b0-3b30-a3a4-57def6d53613 | -15.7922 | -52.26321 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad8513ac-fd17-31cd-b071-189a96996ca4 | -20.12205 | -47.68944 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b62e042d-2108-3fbb-989b-773236ec65ac | -14.17973 | -43.32309 | 2025-09-11 03:57:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4680c655-4945-3204-9625-3fbb7b558350 | -19.37301 | -43.26873 | 2025-09-11 03:57:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6e48f984-5c32-3cfe-9297-c9a524523b2c | -17.84204 | -46.74344 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea3b113e-de79-33ec-adcc-61b6894be210 | -14.36885 | -47.29699 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9e4a81d-9b30-3334-81cc-29bba120cee7 | -14.36077 | -47.29796 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19ec5944-5c79-320f-850f-8fec6126ca56 | -19.99329 | -47.6326 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c891e55-870e-3cc6-84c4-cf52cc6ef67c | -20.05701 | -44.84042 | 2025-09-11 03:57:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad7e4188-1a2f-3314-a85b-bebdc0746d97 | -17.37929 | -52.92338 | 2025-09-11 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3390b20d-c0c0-3239-931e-30b0613cd8f5 | -16.62468 | -49.76577 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 390896d5-8b66-3ff5-8d46-b7d7cb444295 | -15.63064 | -47.53837 | 2025-09-11 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3977147-c033-366c-9624-fda16ea93de4 | -17.9456 | -44.48953 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13c84341-c200-3d8f-aff9-f9f0f47842e7 | -21.2309 | -43.83661 | 2025-09-11 03:57:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fbe27372-30df-3d2f-917c-6877d2896696 | -16.1774 | -48.6866 | 2025-09-11 03:57:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7f0063f-9068-3bb8-a456-82cabbf442b1 | -19.34063 | -41.31301 | 2025-09-11 03:57:00 | NOAA-21 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbec093a-8959-3c9f-80c0-142110d54ea0 | -14.30821 | -44.87013 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 374b992e-bc5c-38b9-9a98-b8bca1d200f1 | -17.37816 | -52.92844 | 2025-09-11 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37fcea17-4a3e-36c3-a008-6dd2a30c5bd0 | -14.13806 | -45.40088 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 516ad4ca-cccd-3029-bef7-78b305fdd518 | -20.06681 | -45.29285 | 2025-09-11 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c05a9f2-d310-364a-b048-51cafb8d90cb | -17.82264 | -44.28135 | 2025-09-11 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 156b341b-8f80-3b43-a64e-3dd7a4ad55ef | -18.40887 | -43.47997 | 2025-09-11 03:57:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4c9c442-7621-3c42-ab16-c3040aae690a | -17.2713 | -46.08156 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 243977fc-0628-3ec7-ba96-d208d9b1b8af | -18.56139 | -46.56119 | 2025-09-11 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07be6447-5f76-38ed-b00f-cb8a24252d3c | -17.90516 | -44.59184 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 031b379e-8562-370b-9a28-e2c690ee410b | -15.22831 | -44.03595 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e24673b-9a62-3914-b18c-bb9459ced3c5 | -20.46119 | -42.84917 | 2025-09-11 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e1e05b9c-451a-3a26-9690-46595436977e | -19.02499 | -46.26502 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2264c315-36ad-3d27-b77b-30a7cf92814e | -19.91022 | -44.34482 | 2025-09-11 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 80db1d51-6a82-3199-a876-7b149f41c333 | -20.08938 | -47.55819 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c59fd63c-df48-3708-955c-d767f6738668 | -14.81404 | -48.28514 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56cc3720-eb42-32f3-86c4-f5f1a975e612 | -15.22315 | -44.04409 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bdd48a6-5fb5-3ced-8f34-1c25e6c1af81 | -18.3447 | -49.33083 | 2025-09-11 03:57:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92ef4a96-3c84-36d5-a33c-cf41eaad58c1 | -14.6186 | -48.85257 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f65d8f46-8b58-33ae-98c7-9dbc6b773eb8 | -14.41178 | -47.32484 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2d135c0-32fa-3887-8587-d851f6ae323f | -19.98714 | -47.61965 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 81a9d6f5-48e0-3396-8518-1042c9455e19 | -17.90863 | -44.58954 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3e432ce-f5eb-369b-92af-23fa7ff2faa9 | -14.13258 | -45.38507 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6928ae75-5e3d-34dd-bf53-8413ab4c0bb0 | -18.76797 | -48.19212 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9d8432d-39f3-3a51-87e0-26e167ae2a8c | -15.78653 | -43.12797 | 2025-09-11 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51b02e47-7839-3ff7-a712-75b7d4fcd559 | -19.99775 | -47.60952 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fc7d3f5-5e7d-39d1-a1d0-dce9fd628736 | -19.48473 | -44.30176 | 2025-09-11 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4fbd0da-b393-36f2-9ac7-cadbc18c2f7b | -19.90554 | -46.90403 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d22b3b23-29c5-3e28-a5e6-089fda07754f | -15.67023 | -47.02978 | 2025-09-11 03:57:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c87d4e12-5802-3f29-8834-cf9940cb6d9a | -19.20875 | -47.9858 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f180c176-3c85-3c3f-9362-335abb84e67c | -13.66127 | -45.72887 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e12a80-32bb-35d0-84cc-13a48a57a6bb | -14.91463 | -47.30216 | 2025-09-11 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e32b4c6-1ced-34ac-8861-a1889203c63a | -13.32641 | -46.37457 | 2025-09-11 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 55118e8f-fd86-30a9-9ae1-703f8813e3d8 | -20.9071 | -45.28924 | 2025-09-11 03:57:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 82fbdfd3-9d62-384a-9bac-9ce8722b6351 | -14.22544 | -43.09296 | 2025-09-11 03:57:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6fb63949-9572-3639-b4f7-8e89e177338a | -16.5856 | -50.08878 | 2025-09-11 03:57:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 289db2dc-1b49-3aae-b60d-92c1ffff3e4a | -17.55743 | -44.55455 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05697878-adcc-313e-8020-1991e8c83de5 | -14.36724 | -47.30582 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 513b79f7-eb76-3cb2-82b3-45f98e4920fb | -15.48309 | -49.36164 | 2025-09-11 03:57:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed689a35-a2c3-3025-b6a3-1fde89a15a96 | -12.95982 | -46.73376 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| beb79db5-3cc4-3cde-9c4c-bfb1cf683e5c | -17.83544 | -46.73864 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5c56473-fb97-3b7c-8afb-7d55761742e9 | -17.76559 | -44.44039 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12f43a75-e8a1-39c4-a575-d3ff016e10e0 | -14.2809 | -49.39635 | 2025-09-11 03:57:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccf420d9-24a0-3de3-bbf1-2808b77221ba | -15.14073 | -52.44623 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10700db5-93de-3e28-ba81-e0c788b473b5 | -17.83474 | -46.74244 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README35.md)
