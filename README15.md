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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbfc2c6f-8c79-3338-b9a7-03d29c44ccc2 | -14.71479 | -48.41346 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 194300a4-1403-31a9-b5df-6593b0f0ca5e | -10.8288 | -54.04339 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abcf78c8-bc3e-328a-a4fb-ed26e8f13d73 | -9.85689 | -55.1623 | 2025-06-25 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71008c4e-12a4-3bb5-ac6a-796a199017fe | -13.04988 | -48.82941 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee2e20c2-2bce-3e87-bb8e-b6ed76bc7e18 | -10.30215 | -57.14053 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bf3d818-9d17-385e-98a1-3d68698a82c5 | -12.58581 | -56.99213 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c44304e-7e4e-367e-9d51-6592630576b2 | -11.57278 | -47.43192 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 496c0a05-d230-3df1-9a7d-59c030c001f8 | -13.05508 | -48.82531 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 845b328c-feb5-36c6-85d6-3e7ca05af1f5 | -13.04088 | -48.82974 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b83b9aa1-b23c-3ac6-aab3-85c0d2ec8c4e | -10.37296 | -54.24748 | 2025-06-25 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 306dadc8-5c5b-3543-a186-24cee559595e | -10.35976 | -57.26246 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f0d578d-c45b-3f66-a14f-3d280e8674ee | -12.79626 | -48.73201 | 2025-06-25 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c5e1f7d-0072-3408-9a93-d99f717c1e56 | -13.60834 | -43.97045 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c7aedc7-217c-374b-b019-e6d248c26410 | -11.94292 | -48.42732 | 2025-06-25 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cce802bd-405c-3fe0-8453-a5cbb2f1883f | -11.80429 | -47.55241 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5085b3c-2c80-3d51-b5b5-8d1fa9bd8c1a | -10.87097 | -54.3247 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01ddf145-4bab-30ec-b79a-271651ffd1a6 | -11.09622 | -46.64254 | 2025-06-25 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6600dd4-1b58-34f8-9f6b-22dcf6af6017 | -10.83831 | -54.04854 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ac18fca-11a0-32d2-955e-a6ce5e1ef560 | -13.6141 | -43.97641 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef7b7e02-6728-3296-ad9c-e9378ba6e74d | -10.60021 | -49.46462 | 2025-06-25 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 485a58c2-2e84-302e-9dd8-7c0a8c95d9c7 | -11.61569 | -46.50439 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 567ec5fd-a32f-3b5a-8175-5d81e09519c3 | -13.04537 | -57.09464 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02429ca7-1f56-3689-aa50-ca878bf97e72 | -10.81485 | -54.04493 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| befa822e-6b84-399f-af5e-a2d0ca0b0176 | -12.80083 | -48.73276 | 2025-06-25 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11a6450e-9035-3359-b4be-978dbbe107bb | -10.83216 | -54.04391 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8693548a-5c33-3f77-8154-3d5b3a7082e9 | -10.23588 | -56.76618 | 2025-06-25 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dba55e0b-841d-3855-8c07-5b6a0dfe2880 | -10.82755 | -54.00631 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34d3cc7d-e2bf-36b1-b803-28de53343291 | -10.86484 | -53.75885 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5946dd9e-9ae6-342b-a567-365d2037599d | -13.04532 | -48.8287 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1762c947-4676-3d6a-8836-2c6fc3392ef1 | -13.04029 | -48.83448 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe9bdc4f-7965-37a6-b495-8908c2ad2500 | -10.36038 | -57.25868 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cad57ff-9f3d-35b0-bdd2-77e9636b8055 | -13.14361 | -56.80403 | 2025-06-25 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5da8c244-e17c-3465-8981-242f47e66b71 | -15.07976 | -48.94501 | 2025-06-25 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc3c77e8-5070-3dda-a992-b3e7f4145465 | -10.85077 | -53.76044 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3ed918e-a1d0-3620-96a9-596f65f8ec66 | -14.15937 | -50.43006 | 2025-06-25 04:59:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9d011cb-5e8f-320c-a4dd-8049d9a8be13 | -12.80021 | -48.73755 | 2025-06-25 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d813733c-53bc-3c87-a827-41659a010b33 | -11.80665 | -47.55283 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aa3c8ba-3761-3a78-a5b3-d3f1524921c7 | -11.86792 | -54.69633 | 2025-06-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a1ffc807-1229-3ac0-a23a-5aa673a6b1e0 | -11.27988 | -52.4648 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60c0855-4b3b-3be9-9ea4-4cf4ed4e80e8 | -10.3616 | -57.25114 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc0308a-93c8-305d-b7bc-3719a1c8d6cf | -10.59598 | -49.46404 | 2025-06-25 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7698259f-edbc-3210-897a-1af66a70ec7c | -12.28187 | -57.26803 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6208b7c7-9a5f-3c48-a4d5-503e82f34a23 | -12.52489 | -57.19871 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa1ad701-4a8f-386b-9535-b4dd47e2015e | -10.29934 | -57.13622 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 592c9cbf-4e8d-3fd7-917b-8e09ee77d77c | -13.04014 | -48.83273 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08978ed6-850c-37ca-a089-5a68b7680240 | -11.94355 | -48.42242 | 2025-06-25 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fa52e70-1cea-3982-bb66-debcecdcb43f | -12.51192 | -47.4337 | 2025-06-25 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbe16e51-0b54-3755-8638-c7777d74d003 | -10.86767 | -53.76302 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b855c105-c701-32e7-8509-71b178e0fc32 | -10.86884 | -53.77816 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6df13db-467e-306f-b061-3ee4d98edb6c | -10.59116 | -49.62724 | 2025-06-25 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa7d997c-cf1c-37d3-889f-ff3b69d13b01 | -10.36319 | -57.26303 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8af1199-6bc8-3e67-96c4-43da16a60662 | -10.82825 | -54.047 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20ea002a-335a-3368-8d98-dcc11169b8b4 | -11.95753 | -47.01704 | 2025-06-25 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fd287de-5e26-3937-83de-6fd1521911a6 | -10.06086 | -55.55585 | 2025-06-25 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fbaac3f-02f8-3505-a604-87798ef4ad91 | -13.29252 | -57.084 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60ca0d0e-d007-3c31-876c-7249762a2ef0 | -11.61651 | -46.49796 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a49c804-fbb6-3709-8c74-16ec8399fa01 | -13.04486 | -48.83519 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f9cfbd15-7a6a-3a02-827b-da42d6d6de46 | -10.826 | -54.03926 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c79e0e81-3572-38fa-bb98-e2364672bec4 | -12.52826 | -57.19927 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59ee2f0e-3066-3270-8d06-fd72ec609e5e | -10.86539 | -54.31652 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a34d1b28-7476-3c8c-ad3e-644c52164409 | -10.83441 | -54.05164 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a94694ab-10af-3ddd-9a17-795533ea8a32 | -11.9509 | -47.02847 | 2025-06-25 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e3469be-9f53-336f-b66a-10f361abe953 | -11.13998 | -51.02444 | 2025-06-25 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b037f605-d47e-376c-8006-0bc192f0c042 | -10.86829 | -53.78181 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03df3ac9-a250-3b5d-b492-e1c2121c9aa9 | -10.87104 | -53.76354 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4110ae66-a557-3380-990a-ccd6d3ba883d | -13.14855 | -56.81588 | 2025-06-25 04:59:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a30f2287-6f8d-3b57-bbe5-8f0025c14a9a | -11.08593 | -46.64087 | 2025-06-25 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b792307f-05f5-3383-ba84-a9243456ec6b | -9.37912 | -57.55804 | 2025-06-25 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ddbba97-477d-35e0-8f8d-dfe0a16cdaed | -10.30275 | -57.1368 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 535fe2de-c741-30fb-b0ae-4c530dfefd67 | -11.80175 | -47.55221 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b2ed339-80ba-3236-9f49-1902015b16bd | -11.13786 | -53.91613 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d596037-a695-338b-a4ea-cdf46a244f47 | -11.61588 | -46.50327 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d5725c1-026f-3ed0-886c-de88e8afd299 | -9.361 | -57.55173 | 2025-06-25 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9cc09d4-135a-377c-9137-0dc1e872bcf0 | -13.04545 | -48.83045 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3356e656-5914-3007-837e-e04202d4da34 | -13.0447 | -48.83344 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25bd3aad-3442-37a4-b4d9-3a1b94a4d60c | -13.04604 | -48.82569 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ab9be84-de3f-384f-8505-2d3659d59e0d | -11.88783 | -54.67762 | 2025-06-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8d0907b-8842-3910-9351-7d49d5304772 | -10.82545 | -54.04287 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6130c461-c2a5-3db0-b64c-b19c8d351d60 | -11.33869 | -51.45581 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 344224b1-c657-3d5f-a3c0-b7b4a1043e80 | -10.83551 | -54.04442 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7455a7b0-4dbb-3dfd-bd7b-56aa410f9935 | -13.04147 | -48.825 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 673fb05a-ede3-3fbb-95ec-58e2a6916b0c | -11.61666 | -46.49682 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5403fb39-23b7-37c8-8906-fca97060e755 | -9.85359 | -55.16177 | 2025-06-25 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 530ae9a8-1b4d-3052-8671-a9149ac7826b | -10.86399 | -54.30585 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d8086f1-94e4-37b0-ab9b-855dab6e07c5 | -11.79941 | -47.55159 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12d36a53-4264-3085-b61b-2dccec808c58 | -14.80783 | -48.29116 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8143f186-18f9-3a5d-8dcf-819855202dcf | -13.29586 | -57.08457 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bffcaa21-9677-36b4-b863-b5967763765f | -13.29369 | -57.07676 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff6402d-864e-3d90-87c6-bbd69b5006ab | -13.05445 | -48.83008 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c00b7a7f-c72a-3c70-8283-74deb8c6fc5f | -11.58941 | -47.61021 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58bd2083-0159-3411-9b74-157d62f762e8 | -13.05001 | -48.83115 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54939deb-7ae6-32c2-8122-8557489a0708 | -11.5878 | -47.61032 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7f68ed4-01ba-3a6d-8b53-30fffc42491e | -14.71542 | -48.40843 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| beec7efb-8b95-3ed9-ac28-820c375e3c19 | -11.14123 | -53.91667 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c833432-301a-3275-9681-b9fa8c29c3e3 | -10.83496 | -54.04803 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d49b25-3574-3fff-ac2c-cf391694de28 | -14.71957 | -48.4143 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90316c23-aabd-33c8-bd8f-c927534ab154 | -11.59268 | -47.61094 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db260dbe-faa0-367c-9860-d4eeb2987783 | -12.80541 | -48.73346 | 2025-06-25 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46daa9d3-b353-3ad8-96fd-77118d48da91 | -10.8221 | -54.04235 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b49bc6e-526f-3187-bd6e-263ab09709c6 | -9.38327 | -57.55471 | 2025-06-25 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README16.md)
