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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53b444b5-a9e4-3b36-9c93-fd8827386b14 | -12.2022 | -50.82167 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 153a1286-5069-31e7-8979-e1cf0c005c52 | -12.20151 | -50.82673 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ca37ea2-347a-3383-b732-c298009ecebf | -12.20082 | -50.83179 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f023a4a-6bd4-3999-9cba-0dd09cceffcc | -13.55076 | -50.3095 | 2024-09-26 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adc6576d-0c65-3f9a-b174-f35ba2e132a5 | -13.27301 | -50.14359 | 2024-09-26 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3430c3f-4763-3c35-9a92-4fbe3e58f52e | -12.67349 | -50.94499 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52f16135-5483-3382-809e-02b520547835 | -12.67279 | -50.95004 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a15a7e6-c767-32b2-b00e-328a7c9c90fa | -12.66888 | -50.94947 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ec0344a-34c3-327e-a23f-1eda1c158897 | -12.62796 | -50.92795 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0c3aeefe-def6-3345-98a7-920289d63022 | -12.62405 | -50.92737 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6231d704-7e6b-3e08-8556-612b2f840d03 | -15.02811 | -51.34788 | 2024-09-26 04:59:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 091a93f1-17f0-33c4-afaf-ae99ced4f02f | -14.8927 | -51.48823 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| db8a30a9-7099-3d3a-89ff-dd8bfcb0c022 | -14.892 | -51.49328 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22f7d5c7-dcd0-381b-836e-7bc5af26dd67 | -14.8913 | -51.49833 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3475b04-c597-3656-876f-3fd04632e98a | -14.8902 | -51.47754 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f9513ad-e737-39c2-b9ad-7e2936af04a4 | -14.8895 | -51.4826 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a00fe699-2fc1-3231-925c-6865bded5f58 | -14.8888 | -51.48766 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e0364f9c-d7c3-3184-9665-d50e1cdf8996 | -14.8881 | -51.49271 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b747ad8-ba15-33e8-93f8-dd3a9b413f23 | -14.88741 | -51.49776 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30bd32b2-47d4-3f01-b7f5-93019b554cbb | -14.88671 | -51.5028 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aee92613-272e-3f1c-8524-717149542582 | -14.8863 | -51.47697 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3698e93c-892a-3339-8b17-f26a04f453b5 | -14.8856 | -51.48203 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5fd242be-30dc-375b-9f2a-ec8a0850ff4c | -14.88282 | -51.50223 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cde98c59-7cf3-36a0-943a-27005a527472 | -14.8824 | -51.4764 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3baaa099-68c5-32fc-8086-90f2ec37371f | -14.88212 | -51.50727 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f3a8ae9-06af-3309-b0a7-31b42a96e441 | -14.88171 | -51.48145 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4e8680bb-edec-3b0c-a670-b21a22091b99 | -14.87851 | -51.47582 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b25fcf18-6d65-3a69-8fd8-5a0655bdee01 | -14.87823 | -51.5067 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c296d414-55c3-338a-8e1f-750627c465fd | -14.87781 | -51.48088 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d82948be-7a53-33cc-8fc8-bdb2fbc2f00a | -14.87461 | -51.47524 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 81f3784f-5573-34d4-9583-19925ac72e36 | -14.87434 | -51.50613 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3c46ebe-f53f-3c48-aaf8-c7a502168152 | -14.87391 | -51.4803 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4be178eb-452a-34ae-832c-17bc6d40ca90 | -14.87365 | -51.51117 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b2d6698-f13b-323b-8c6c-73bbde7d5397 | -14.87322 | -51.48536 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8269ee4-47a7-383d-9d6a-36a7b93de850 | -14.86976 | -51.5106 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e8e3a20-aae8-3cc3-b641-ee893dc8e004 | -14.86933 | -51.48479 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6bce7624-200c-3027-999f-d14cb9e651c3 | -14.86864 | -51.48984 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92b35909-3635-3d67-a334-6fe2a6d9715b | -14.86587 | -51.51002 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b611fe19-7021-30df-9d8d-1e716353735a | -14.86474 | -51.48927 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 01730cef-aa4f-384e-9a19-4df6fd5c678b | -14.86405 | -51.49432 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b6bdeb9-14ee-3bbc-ae4e-454f1cf3a062 | -14.86336 | -51.49936 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c577dc7-7a08-3e50-b19c-929bf5c4192b | -14.86267 | -51.5044 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30b8a1c3-58d5-3701-ae2a-83ae18155f20 | -14.86198 | -51.50945 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a9e70d2-a7c3-3c9d-aee6-99707e8de74a | -14.85947 | -51.49879 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69cb7d83-3215-3a77-b9ac-bf8109e93694 | -14.85878 | -51.50383 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf07be80-ffe0-3587-b1af-643186554d70 | -14.85809 | -51.50887 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c068dbe1-956b-30c4-891f-10e32250c83c | -13.94433 | -50.86868 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2316dd6e-005d-36aa-90f5-db659b2ed8c8 | -13.74251 | -51.06126 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb2bfea4-648f-354c-b156-e47d07862890 | -13.7418 | -51.0664 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f454100b-b38d-3640-bb71-5a8c86db449c | -13.74109 | -51.07155 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a877135-6c7b-33ac-adcf-fdb073d1b8cb | -13.74038 | -51.07669 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e34fb97-f128-3701-adf7-bead4e76a03f | -13.70567 | -51.06635 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c8d50b2-a538-3f38-8f8c-0f3ddd5aef0f | -13.70174 | -51.06578 | 2024-09-26 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a22d55f7-edda-3baa-938e-1b32d33939c2 | -10.68563 | -50.69937 | 2024-09-26 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bed7edf1-95d0-37e6-a401-896039681e19 | -10.676 | -50.99228 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d33d05-2982-3837-be4f-8eabdd9aa851 | -10.61391 | -51.12797 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c119c6d6-08bc-3d1d-b28a-7a2ad759c63c | -10.61082 | -51.12278 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecff095a-d09a-31da-83ec-f2991498e9c5 | -10.61015 | -51.1274 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9990c628-ed3d-3ca8-b6f0-570d1c225b8b | -10.60773 | -51.11759 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7930da29-3d7b-31a6-ad54-31c9b02545ea | -10.60706 | -51.12222 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21b609ab-24e0-3a8b-9e76-ce899385a9be | -10.60397 | -51.11703 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc7525ca-1f7a-3e0d-9668-15130f8f4508 | -10.60087 | -51.11184 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7ff475f-2f80-3534-a54e-6a7ecabbf6b3 | -10.57384 | -51.11258 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bab6bc6-fae4-3331-83a4-42c87ad68d21 | -10.57008 | -51.11203 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84b37223-4ed8-37cc-9b63-ef0267d6d011 | -10.56631 | -51.11148 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de0694ce-2209-38d9-ac61-7d5510b3beb7 | -10.5632 | -51.10629 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f27532a-d526-3f25-8dd0-720e6148c5b1 | -10.56254 | -51.11093 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2781f467-6ea5-3fd2-ab12-f85b68652ce2 | -10.55944 | -51.10574 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5824e58-cce4-3019-a9c6-5ca24f6e501b | -10.55567 | -51.10519 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c070a194-23b1-34f0-8ba6-8d676cf0d5fc | -10.5519 | -51.10464 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bede3fe-a762-3981-97ea-4b57361d7ca8 | -10.54813 | -51.1041 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d095c441-494b-3158-8dcc-ddcbe8ffb93f | -10.5437 | -51.10825 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55aae43b-be02-3d4f-a1c0-f5ce8920e62f | -10.54304 | -51.11293 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a4523e8-e35d-30f1-8cda-c0c47e030808 | -10.53926 | -51.11255 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57ebd639-00d1-3f29-bb50-fb6cf98f0a6a | -10.53859 | -51.11727 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 145b0d07-41ea-37f2-b602-33d81d72c683 | -10.53349 | -51.12621 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8507c393-94ee-3e77-affb-9dd260ae4e80 | -10.52908 | -51.13031 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0f9c4aa-ec55-3642-bddc-c7208ce6099a | -10.52844 | -51.13479 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 966165fb-89a6-3e46-8a3c-15e9af76bab4 | -10.52144 | -51.15728 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 978cddac-620e-320a-b6b0-91cb77ceb23d | -10.52077 | -51.16205 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc9168e3-c54e-34fd-aa4d-6c024630e43a | -10.52067 | -51.15515 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 651e294f-a63e-38ae-ab6f-dfbbf671a1ce | -10.52022 | -51.18422 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5b356b6-aa40-3c7b-94c1-76d7ae2553b8 | -10.51997 | -51.15992 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7d74a880-5800-3204-aa30-fc32933ee26f | -10.51808 | -51.18129 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af978b13-107b-35c7-a026-35d5b7ac7973 | -10.51766 | -51.15698 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34ff41ad-9dd9-3074-924a-7a8e360716ac | -10.51744 | -51.18588 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f4310a8-b15c-32ea-ba97-aa9cbe5b2a24 | -10.51713 | -51.17921 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92631039-81ae-36e3-9fae-8b4c28733c6b | -10.51698 | -51.16183 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 220d7fe4-a408-329b-94f1-e7eeedc7880f | -10.51645 | -51.18379 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93ccc97e-07ce-33a8-a467-197d49acb07d | -10.51616 | -51.15976 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b08c833-433e-3389-a4ac-00524c7f0398 | -10.51544 | -51.16463 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93e1b5aa-d335-3157-9712-ff0f5408afb2 | -10.51386 | -51.1568 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eaf299c-9f81-3b16-a507-7d770501802c | -10.51165 | -51.22691 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4eeb88-5e3c-393f-bbbf-6eba4e7067f5 | -10.51104 | -51.23121 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 834b2c6f-26dc-3c95-b732-496dff144abe | -10.50978 | -51.22907 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d12f2c0-19df-3eb6-8e69-b21591ddfd27 | -10.50865 | -51.1587 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e402e627-04af-3ae0-a938-a06961609153 | -10.50732 | -51.23051 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cec0fa9-4d45-3551-b81e-efd1a84208bb | -10.50607 | -51.22835 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a5d2ff2-d8e9-3181-a08a-03ebcbb64f5e | -10.50495 | -51.15781 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68e10e5a-598a-39e4-a358-e86be3dbaa95 | -10.5036 | -51.2298 | 2024-09-26 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README117.md)
