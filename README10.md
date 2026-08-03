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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef2c2182-3aa8-313e-8ad9-02e3a8f695de | -5.95783 | -45.02089 | 2026-08-03 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 96bdf894-5ced-3bf9-91a5-52d39a49024c | -8.1866 | -49.19806 | 2026-08-03 12:00:00 | TERRA_M-T | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ecb74895-4db4-341a-9e3f-bc2b9ca3772a | -7.53458 | -45.07352 | 2026-08-03 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 337dd080-87e7-32d5-ad8a-9fdea2306c16 | -5.96953 | -51.39077 | 2026-08-03 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5fec7eb0-fefc-30c1-9445-97758153fcbb | -5.90543 | -44.99958 | 2026-08-03 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 29ec9986-9418-3258-8f9e-1c6d0f70e2ae | -8.34762 | -45.97766 | 2026-08-03 12:00:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5197348c-9b75-3bfc-962a-fd468a067b7a | -11.58009 | -50.23108 | 2026-08-03 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 911676b7-e27f-35cd-be98-6a1351279954 | -7.39891 | -45.06455 | 2026-08-03 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 84792009-0bf2-3eeb-b2e2-977a33de4a7d | -5.96809 | -51.40059 | 2026-08-03 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c9917c69-4902-39ae-9266-b8644533b5a5 | -7.52931 | -45.02896 | 2026-08-03 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6ff2efc4-b1c7-3b9b-ae86-85980044c6a5 | -15.69503 | -44.38029 | 2026-08-03 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 22bcceab-6331-3cf5-ba18-5c2dcfe5ff28 | -14.27153 | -45.24953 | 2026-08-03 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| e104f149-325a-3ebf-8a80-899c30e2fb81 | -7.52986 | -45.03499 | 2026-08-03 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f5d5ab09-3fab-3030-8af2-1c62280970cd | -6.55699 | -55.15842 | 2026-08-03 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 26f7339d-6f03-337b-9ca7-5ad750036395 | -5.48645 | -45.10647 | 2026-08-03 12:00:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d18bbf6a-e948-36e0-85db-9730bf9d2839 | -11.13351 | -50.39801 | 2026-08-03 12:00:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3befe6ec-7232-38d9-8466-ec17fbe660f3 | -10.20705 | -50.09735 | 2026-08-03 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ea89604b-dbeb-3c84-af72-61eea114f7bc | -11.45031 | -50.17865 | 2026-08-03 12:00:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d085f1d5-c3c0-37ac-bb9c-a80d7683611d | -6.86121 | -44.79572 | 2026-08-03 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c45b5707-97f5-32b9-8dbe-e1f484b8aed1 | -12.20129 | -52.86346 | 2026-08-03 12:00:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 53d37e90-f832-32a4-b4df-1fe630eb89b1 | -8.55239 | -47.74867 | 2026-08-03 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 817e07e6-21de-3343-8193-6615a2cc0ba5 | -6.09138 | -45.06498 | 2026-08-03 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8160230e-edc5-31ab-a98f-a139c5d8f06f | -7.97021 | -44.90644 | 2026-08-03 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| e288278d-7753-37f9-b772-35358d7b10ca | -5.48463 | -45.11974 | 2026-08-03 12:00:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| fe57c9f6-1999-3c2e-ac28-3b3fc7732abe | -10.64853 | -44.73474 | 2026-08-03 12:00:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 055b5b6f-5c7d-3e0e-9825-240c0a8e0df5 | -10.61474 | -46.51783 | 2026-08-03 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8ca89945-306b-3742-9ce9-061efcee5304 | -14.26315 | -45.27962 | 2026-08-03 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0b39b906-143c-343d-b612-415324bcdadf | -7.96824 | -44.92147 | 2026-08-03 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8ce47942-4acc-3b61-a483-e72ec040ddf2 | -14.26534 | -45.26144 | 2026-08-03 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 0aecb4aa-a035-3957-803f-5ce44a516e51 | -5.95597 | -45.03454 | 2026-08-03 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d4823a56-492f-3246-912e-0c65d86a065e | -7.38785 | -45.06298 | 2026-08-03 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 90640dcc-b210-34a3-911c-7c4d9e2e81e2 | -10.62361 | -46.75233 | 2026-08-03 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 04d3a8da-a460-35ec-a05a-8575e0d1343f | -9.92006 | -53.30124 | 2026-08-03 12:00:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8b36116-ec6a-3eb1-8bf7-7da08e772a84 | -15.69261 | -44.40238 | 2026-08-03 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1332cad4-c72b-337b-a9af-28686a25d65d | -11.53346 | -46.89592 | 2026-08-03 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b2ac24e5-852b-3b57-8efd-514e64914c5a | -6.06616 | -49.25686 | 2026-08-03 12:00:00 | TERRA_M-T | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f795c51d-396a-3cab-b1db-5e8c74bbb88f | -11.58136 | -50.22211 | 2026-08-03 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbc8430e-0199-3b8a-8b11-950f0d1d6b84 | -14.2695 | -45.26755 | 2026-08-03 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 58e3ac32-71e6-37f8-b567-81e48eb7607d | -14.26749 | -45.24348 | 2026-08-03 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1ba94d09-9b61-38e6-b91c-f888dfe680a9 | -10.64639 | -44.75183 | 2026-08-03 12:00:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8f4a61fc-4974-3cef-9ba3-ae059cfc1e56 | -10.6164 | -46.5052 | 2026-08-03 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5d650cde-796c-3b41-b98c-f0caa74d8a87 | -7.56319 | -45.03973 | 2026-08-03 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0863e7d2-aa55-352f-b2c4-48245f73a945 | -6.06695 | -45.05558 | 2026-08-03 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b0881448-fe80-30d6-9a5b-219bc72a43b7 | -10.58042 | -46.77811 | 2026-08-03 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c3eeed0b-d251-363f-a9e9-0a6943e4ca42 | -10.63226 | -46.76604 | 2026-08-03 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 06b63aa7-35e7-3e79-8711-e6da3c7322a7 | -10.1476 | -46.3358 | 2026-08-03 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0f523035-afe7-3143-95fd-4ad7175d9037 | -8.54717 | -47.74151 | 2026-08-03 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a3cbd90d-6f0d-3251-8366-e6a43ea9e8b5 | -12.51054 | -50.362 | 2026-08-03 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fba0642-d403-34ac-a2dc-f00617a03f7e | -21.64039 | -46.3773 | 2026-08-03 12:02:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 8c83d213-9f56-3c68-9f18-9c2c049869cd | -17.05313 | -45.04303 | 2026-08-03 12:02:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 2597a156-cd5d-39ad-bb9e-74a8b3348042 | -17.97371 | -44.57818 | 2026-08-03 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 450102fd-732d-35d2-868b-931fb8935b36 | -17.96012 | -44.57653 | 2026-08-03 12:02:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 6fa6b70e-70a0-3c8c-8750-6468267a3d89 | -17.05188 | -45.04858 | 2026-08-03 12:02:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 76a800b1-475c-3bdb-86da-b657bd3182fc | -17.05409 | -45.02777 | 2026-08-03 12:02:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 09593e1b-9477-38e4-867e-5b12e72b8177 | -21.64258 | -46.38309 | 2026-08-03 12:02:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 0cfe7c58-c896-31ce-9396-925014927cc5 | -17.05549 | -45.02225 | 2026-08-03 12:02:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 065a9791-c3af-3893-9244-8ae78e5b963a | -16.39036 | -44.55463 | 2026-08-03 12:02:00 | TERRA_M-T | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| db5414ef-460e-3372-a634-39a08d4b24c6 | -20.56644 | -45.18887 | 2026-08-03 12:02:00 | TERRA_M-T | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 41ba6430-8484-3e17-b23c-0a634433d973 | -16.3808 | -44.54832 | 2026-08-03 12:02:00 | TERRA_M-T | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cc95daf3-75b8-3b4f-8f76-1bd2b72705a1 | -15.64846 | -53.87086 | 2026-08-03 12:02:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a1fd347-c828-3613-8a08-a721a03b8c02 | -7.9532 | -44.9188 | 2026-08-03 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7aec4625-3585-3fdc-bdfa-2b8e9a3a1ca7 | -5.9631 | -45.0236 | 2026-08-03 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3bbdd66a-6417-3852-a615-6bf3ad286895 | -17.0616 | -45.0191 | 2026-08-03 12:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 7a9025a0-81a2-36b4-8810-ecc69eb0281c | -7.9721 | -44.9169 | 2026-08-03 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.1 |
| c8ffec4a-eedb-354f-88ff-75ef6fe9eb53 | -17.0616 | -45.0191 | 2026-08-03 12:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 9ee0a7cd-7672-3543-88be-9c902811e2e2 | -7.9721 | -44.9169 | 2026-08-03 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 9fdf3c55-9a95-3240-a4e3-2ad196613cb9 | -17.0609 | -45.043 | 2026-08-03 12:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c5487462-c114-3969-93ee-c9745772a312 | -7.9532 | -44.9188 | 2026-08-03 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 73e02214-9ae8-38a3-9d89-36b4c5b38e2a | -7.9724 | -44.8941 | 2026-08-03 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 4dd64487-364c-38c5-9314-332d6d3fc237 | -7.9532 | -44.9188 | 2026-08-03 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 5440da45-2ab3-3ba8-865e-28fbeafe9cd8 | -17.0609 | -45.043 | 2026-08-03 12:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| dfad71c5-1ec3-3509-a039-66892f48917f | -17.0616 | -45.0191 | 2026-08-03 12:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 27df4d37-df32-3b27-9161-05cd9410c700 | -7.9721 | -44.9169 | 2026-08-03 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 344.1 |
| 217971d1-06a7-39b0-8dd5-3fa49f3ee5d7 | -17.0416 | -45.0234 | 2026-08-03 12:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 68464649-d999-310d-8644-4c24c1b39be8 | -17.0616 | -45.0191 | 2026-08-03 12:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 537eb6fc-af30-310c-b393-de941494026f | -7.9721 | -44.9169 | 2026-08-03 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3e5fab08-0b2b-3664-ae93-bc81b1bb805f | -7.9721 | -44.9169 | 2026-08-03 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 333.6 |
| 9d13bfaa-067f-3398-b0d3-2cb77fc26b38 | -17.0609 | -45.043 | 2026-08-03 12:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d519d96e-3207-36d9-9218-fae2d18a3618 | -17.0616 | -45.0191 | 2026-08-03 12:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 32654a5a-6a6a-3db3-a037-be8526543d4f | -7.9532 | -44.9188 | 2026-08-03 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 80eff2ba-5bcc-3dba-b912-6c7e4d14a218 | -11.6047 | -50.245 | 2026-08-03 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d27fd0aa-2c94-3407-8420-f1977a09a17d | -3.1158 | -47.9232 | 2026-08-03 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4ed93eee-c98e-3baa-b1e9-f6a799f29071 | -17.0416 | -45.0234 | 2026-08-03 13:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 9eec695e-75bb-3c8d-b122-16bd3a6fa117 | -7.9721 | -44.9169 | 2026-08-03 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7772f440-7a26-3cf9-9aef-c2a9a4c472fd | -3.1158 | -47.9232 | 2026-08-03 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 166992b9-5b74-3218-962c-1bf8dcc1de80 | -17.0616 | -45.0191 | 2026-08-03 13:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 66686897-a48d-308f-b471-136008d49e5f | -11.6047 | -50.245 | 2026-08-03 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 62721111-4cc4-3037-bd64-094524c0817f | -3.1158 | -47.9232 | 2026-08-03 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 986687d9-7585-3b70-bd51-f51af817889c | -7.9721 | -44.9169 | 2026-08-03 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 169.7 |
| a35d5495-6816-370a-9917-65dcd36613b7 | -3.1158 | -47.9232 | 2026-08-03 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| fd27fab7-d1e0-392c-9da5-d7af6772f5e6 | -11.6047 | -50.245 | 2026-08-03 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e904a684-0dcb-3930-a5c9-ea1eb450b1d8 | -17.0416 | -45.0234 | 2026-08-03 13:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b602b78e-6f20-3e86-b290-70f9b8fa625c | -13.6782 | -52.0 | 2026-08-03 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 39ad294a-d9bd-3058-97c3-f0e610c07821 | -7.9721 | -44.9169 | 2026-08-03 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 4ec20d6f-ad92-3f51-94a9-18710b939f5c | -7.9721 | -44.9169 | 2026-08-03 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 97e4b49c-d353-3a81-9ade-0ce33536e48e | -3.1158 | -47.9232 | 2026-08-03 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 5415b28f-aab5-3fb9-a87d-6118aa73e677 | -11.6047 | -50.245 | 2026-08-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| d7a82d71-a3e4-3061-bed4-74cc9c96fc80 | 0.91086 | -63.00413 | 2026-08-03 13:33:00 | TERRA_M-T | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 0845e904-a4ac-365d-8572-0434314289d5 | -0.47737 | -64.14312 | 2026-08-03 13:36:00 | TERRA_M-T | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 918dd0c5-999a-3c38-bdb4-f877654e7845 | -7.9721 | -44.9169 | 2026-08-03 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |


[Clique aqui para ver as próximas entradas](README11.md)
