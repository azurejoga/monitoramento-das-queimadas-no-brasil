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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 193dc365-cfd1-3d79-98e7-1988aa193b37 | -9.34584 | -63.5616 | 2026-08-17 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e811ebb0-5375-3e3b-91a5-befed05d939d | -14.44353 | -51.972 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52137644-ca22-3c89-8706-1837239b6495 | -16.75834 | -49.36917 | 2026-08-17 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71c00d4d-d012-30d5-80bb-0f1391f6d17e | -15.91531 | -55.54554 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| c8b2278e-c054-38fd-9d23-0bb7fe29f130 | -13.51606 | -46.24564 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a12e742-dc7d-3db7-8b87-2cd19d2c1954 | -16.67186 | -49.45473 | 2026-08-17 05:18:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12e80626-e9bb-316b-aada-24fa7974d201 | -14.09653 | -58.44009 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf9fec68-8ae9-3af5-9f3a-1f4702ef17dd | -11.7112 | -54.60833 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 519371e7-6cce-31c1-90f9-e152eeec25fb | -12.04064 | -46.48356 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b03f202d-d198-3b34-bcc7-42483f69a32a | -11.1413 | -49.04437 | 2026-08-17 05:18:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72833706-6346-3bfc-ae9f-8824a1909a50 | -13.78556 | -53.80255 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8175d9a3-d072-3d34-a232-13918533a2fc | -11.49834 | -46.61786 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cee17769-87cb-3b31-a164-ec094c4cfe8a | -15.16105 | -48.62623 | 2026-08-17 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b1680d6-4612-3ddb-ab83-2a79c83f879f | -11.81125 | -44.81357 | 2026-08-17 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a5bd9ea-eeb6-3abd-8aad-78e964d59150 | -15.81745 | -55.52245 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cb4af86-ec4a-3c95-8360-23dce50e9f0d | -14.02758 | -53.61929 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e718fa91-ddad-34a1-ac83-f9fdfb49b2ab | -14.49913 | -59.3214 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 516ff5d1-bd05-3800-81a1-43a6d600fba9 | -13.43074 | -57.05996 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3586a1ad-ebed-35c7-be39-13f332dc738d | -15.12816 | -50.05494 | 2026-08-17 05:18:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3cc803a-7805-3482-99ad-b4f8e87ddeea | -11.72645 | -54.61052 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5fbdf8b-bd74-3edb-9e71-4197df23b177 | -11.31834 | -47.00542 | 2026-08-17 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7ed7ace-ff99-3c55-8938-53f7d0caa102 | -13.51183 | -46.28417 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a89360c7-78f1-344c-a932-ab7d8fa8b228 | -13.50167 | -46.25283 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 729578bf-7009-325a-8c96-455891c79921 | -12.54918 | -47.85779 | 2026-08-17 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e764231-df8f-3508-984f-00eca46ddd35 | -15.86451 | -56.3455 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ba4cdc8-0a78-3440-a5d4-a8e90ef849ba | -11.72333 | -54.60524 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76ea5e24-88a0-30e5-aa5b-1a303016cdd8 | -11.49679 | -46.61798 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e78c556c-c481-3413-bdae-e8831139ad5d | -11.80987 | -51.77534 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1b45c91-c905-3ecf-8192-0ec54c412c0a | -11.05867 | -62.56151 | 2026-08-17 05:18:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78568243-0c24-3b00-a5cd-5dbcd9cca804 | -15.91287 | -55.53529 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 220009e2-5529-378b-ad68-f1842931f287 | -14.0932 | -58.43955 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e4c636bb-d57d-388d-b872-f7df0b9b27a6 | -13.51442 | -46.26057 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f44867d-6b1c-3c74-bbcb-acc0296cd9ef | -11.70983 | -54.61778 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eebf0a9-c825-38e5-bafe-96e6a9a18a12 | -14.18898 | -53.05649 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94c498fc-a996-3249-a308-02913d0b55db | -12.04795 | -46.48169 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9adaa5a-3e28-3f09-a5cb-aedf5ab463e9 | -14.87335 | -46.64184 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 37806afe-bd15-3af6-a6f1-ef6fab83eef7 | -11.48179 | -46.58021 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc72b8ad-b813-3123-974e-3f239efdfe1f | -9.73349 | -60.74601 | 2026-08-17 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fe1c35e-3b52-326c-8e58-84f33cba1fe1 | -12.66043 | -48.51536 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b402320f-7cf0-3595-9b90-3fbe5e3c3fc5 | -11.20956 | -54.81884 | 2026-08-17 05:18:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f4382c0-ca5b-385d-b065-6f8f58468804 | -15.92054 | -55.53612 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 54c1f053-a391-3b62-95b0-20720dafb604 | -11.7029 | -54.6119 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d07a1c15-4ccb-35bd-8b1c-2ab4fe5644fb | -11.50056 | -46.59851 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f8fcae3-ddfa-3267-be62-b8edd3ef6e60 | -15.82469 | -54.21671 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da94a516-b931-3c8e-a9a7-b9472b07fe4c | -16.41127 | -49.63111 | 2026-08-17 05:18:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d522dec3-0b57-353d-a9c3-959b503b0aec | -11.79547 | -51.7782 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 496d5342-3237-31f0-bcbe-a53154e9cd16 | -15.90065 | -55.53917 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d528544a-a9e5-37bd-a2ee-ea15ef38365f | -12.71191 | -48.47799 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f63b1d9-f15e-3d85-8b2b-06b4a5ac4ff3 | -13.82289 | -53.76403 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f3f5630-7517-3951-827e-f2f36a482b94 | -10.94252 | -57.15308 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3deffeaf-d1cb-373f-a4d9-17ca40ef0ba7 | -15.91984 | -55.54103 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 864a018a-c367-37b4-b947-e3ef047ac9ae | -12.03333 | -46.49347 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 09e6b99a-6043-3086-a4e8-1c27bb84f00e | -11.80914 | -44.8067 | 2026-08-17 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba6c9608-731a-3def-8bdb-1a6cf137f1fb | -14.28651 | -53.06392 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49e3e3df-99a9-3256-8d70-0830c6df5a94 | -11.3915 | -46.39789 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecae526a-7009-3853-b088-4003a43aa678 | -12.66706 | -48.50891 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4041af9-5db1-3ac8-b6c7-9c0ee10f8a27 | -16.71934 | -49.13259 | 2026-08-17 05:18:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39bfc11c-9202-31bc-9491-65ee9484a3e4 | -9.12873 | -66.97277 | 2026-08-17 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 467749d7-e222-3ff9-a307-b14dfdc708ba | -14.86851 | -46.66357 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4598ef8-6884-36f8-b976-be7ce4076f95 | -14.39154 | -56.40088 | 2026-08-17 05:18:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d48977cc-d78c-3f8d-9a30-cd9d5874f727 | -11.32401 | -47.01101 | 2026-08-17 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4986b29-c0f9-3d1a-b5e0-eeab75e30e45 | -14.28708 | -53.05964 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acc9ab59-4e74-397b-a3ae-3c1996af6f9b | -11.91325 | -55.44524 | 2026-08-17 05:18:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcf2a532-a6e9-3638-a933-8b46de5f684b | -13.41813 | -57.05005 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32acdb06-fa14-3b64-9c46-0ced3c1018a0 | -9.47453 | -60.51007 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00b3a8e6-f867-34c2-896a-ec600a5b8cd1 | -15.90973 | -55.52995 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33ebbe28-508e-30d2-ba4a-c4b2be7dec9e | -12.6724 | -48.51353 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6528feb1-c669-3f4d-987e-cc17f184b23e | -14.49801 | -59.3285 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cf7e5011-26c6-33d0-a73e-72cba86f84fa | -10.04373 | -62.45395 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afd999a3-dbf5-3ad4-8593-81d2736ebf40 | -15.12303 | -50.0519 | 2026-08-17 05:18:00 | NOAA-20 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06f583b6-c5c5-36db-9179-3ff95129423d | -12.32804 | -47.24848 | 2026-08-17 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b75d6524-602b-378b-bd0b-52eadb5907bd | -9.32906 | -62.33878 | 2026-08-17 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b6756a8f-032f-3551-a90a-d2c6d86a4670 | -12.55021 | -47.84901 | 2026-08-17 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e30020f9-e9a8-3476-88b7-57c15b49e0ed | -15.91601 | -55.5406 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bf0a35f0-0149-3ea3-aaa8-26890bb3be81 | -13.50767 | -46.22215 | 2026-08-17 05:18:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4638def1-3402-3e5d-8388-8b523aa5c4f4 | -11.82429 | -51.7724 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3292dbd-f61e-3060-8b46-282a8dd11c7c | -14.09375 | -58.43595 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d2a7c12-dc6e-3773-8d0f-b16d065b33b8 | -12.5497 | -47.85335 | 2026-08-17 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f29a3fb-bddc-395b-82ab-ce2a3e26dfad | -14.10097 | -58.43344 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 50581f92-aea8-3ae7-a7c4-0ac08ec9ee7a | -15.7314 | -56.12332 | 2026-08-17 05:18:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6cf4b151-26e5-31f0-9c68-07a135629e6a | -11.32074 | -46.21083 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2257ec7-200a-360b-98f2-ce5c1bd9fb2e | -11.72264 | -54.61 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 974341a5-1e06-30e3-9a24-e82322912a71 | -10.0475 | -62.45461 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6ca260e-2728-31f2-a671-972f49932350 | -11.3911 | -46.40305 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8736fe7e-18d6-3a69-9132-4209d5616e62 | -15.83402 | -54.20978 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31f5c2af-4a83-3fdb-9c2f-78dbe0b7bfb5 | -12.66134 | -48.5076 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6e48e95-0c4b-3103-81cd-554da32378a5 | -9.47233 | -60.50184 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf91f19b-a036-3422-817f-5a108cbf27e1 | -14.43817 | -51.97645 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74f92952-7dca-3221-a5ce-bd3f257289a5 | -14.08821 | -58.44979 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 512f1b71-ee76-3c6e-930c-3271299634c7 | -13.5179 | -46.29069 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8caf7914-7b64-3e24-8502-7efb60359552 | -12.65516 | -48.50799 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83d73b6a-fc48-3115-92c8-dc5c996d3f06 | -9.59793 | -60.52973 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 026d7079-250a-3cc5-a02c-c0a89ee9996e | -11.49973 | -46.59373 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b169abd3-f45c-3aa9-8ee9-b996e3d52cda | -14.41576 | -53.07332 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef96bad8-7530-3341-95f6-adf8db45bd9b | -10.0716 | -60.50397 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa53a14c-31b0-30a5-a9c0-2ad94c0385b9 | -13.78332 | -53.80859 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59b76041-282b-3812-90d4-46aa1dd68d9d | -14.08986 | -58.439 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e080af3-61b5-3490-87a6-5b9fd19dc9bd | -11.21671 | -54.01568 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f8d3b91-a1f5-3cfc-b248-2fdb67685aa6 | -14.45125 | -51.83722 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f74fd3a6-dd1b-3e1f-b066-aef715bf8ecc | -14.86556 | -46.6516 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README55.md)
