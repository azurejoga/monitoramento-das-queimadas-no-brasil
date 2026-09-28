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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0cdd2c0-f7c8-3993-abb1-c2fe2d2d2185 | -20.7 | -57.97 | 2026-09-28 18:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8b0cf8b1-9235-3eed-8e26-28dd6b6fb1db | -7.67 | -44.91 | 2026-09-28 18:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c995107-a698-3a87-a82b-a5ef895856c2 | -10.83 | -57.18 | 2026-09-28 18:15:00 | MSG-03 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 530e2c26-200d-3be6-a70d-732f585e939a | -11.92 | -50.88 | 2026-09-28 18:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4af336f-1641-3790-abde-a208c3e1d38e | -5.73 | -45.18 | 2026-09-28 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a750b4e-4020-3b05-867c-86553b321953 | -7.67 | -44.87 | 2026-09-28 18:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 036a8fc7-6ce8-33ff-a410-38e64a7feb0f | -9.79 | -48.23 | 2026-09-28 18:15:00 | MSG-03 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44546bb9-053f-3201-9ce1-5a6412f258c6 | -11.89 | -50.93 | 2026-09-28 18:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da10625f-7b6b-3a9f-afb7-5dfa8e94693e | -11.92 | -50.94 | 2026-09-28 18:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67c9ca98-842a-3147-9e70-73d8df794029 | -15.4003 | -47.9035 | 2026-09-28 18:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 837876bf-8bfc-3d7d-8f88-e6ef61727582 | -7.9082 | -54.7597 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 9606e705-f20c-3980-8fce-8e05bccf9bea | -10.8189 | -57.1993 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 495.5 |
| 6f082da4-34f9-3aa8-b411-e532f9a7e405 | -11.7178 | -43.4623 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 84e51c93-70aa-37aa-876d-0c4b858347dd | -10.7064 | -44.4317 | 2026-09-28 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 95144d77-f06d-30d1-9d92-81520c979be3 | -12.588 | -51.9617 | 2026-09-28 18:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9f6054c3-eb19-3300-a2dd-8da4bded68ea | -10.8379 | -57.1781 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 205.6 |
| 2892126c-f0bd-35f0-9297-6a745960f545 | -8.2482 | -45.4356 | 2026-09-28 18:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| eab30577-0014-3e31-ada9-caf0cc642176 | -11.1962 | -44.8037 | 2026-09-28 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| ece437fd-d49f-395a-b178-3976ead29655 | -7.7038 | -54.7521 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 61b415d9-d1bd-345b-8315-e092b04afc33 | -10.8185 | -61.3998 | 2026-09-28 18:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| dac3744b-7b76-3648-ae82-254bcf15aa70 | -10.8187 | -57.2192 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 247.2 |
| cc503a27-3440-34a7-870d-82d1561817c5 | -12.6262 | -51.9573 | 2026-09-28 18:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8663ebee-f0b8-3346-83ef-95290855a062 | -7.3306 | -54.995 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 71a0bc75-3d2d-3472-a520-f3234075d14d | -11.0991 | -51.1111 | 2026-09-28 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 71ce68fe-27fd-3c40-b64e-6ba095520d69 | -15.3998 | -47.9261 | 2026-09-28 18:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5e85c19b-c503-3c6b-a35c-4dfcfa2e6a28 | -11.6793 | -44.5246 | 2026-09-28 18:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| f34cbdd2-2d41-3886-a1a8-0e8d10b91343 | -8.2293 | -45.4375 | 2026-09-28 18:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0457e03d-d940-3d0c-b128-89c81bf0bd97 | -13.6866 | -56.6131 | 2026-09-28 18:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 5cd00b24-5c85-3c54-9179-c2d35edf565f | -5.7388 | -45.0172 | 2026-09-28 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 7eab1b56-36b6-33c9-a7fd-7764541ec651 | -14.111 | -46.3063 | 2026-09-28 18:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |
| bfb57962-fa98-3520-84c6-e074aee4752b | -11.1771 | -44.8064 | 2026-09-28 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 250.2 |
| 3e55b011-715e-3379-9748-4b379f1c0782 | -12.4351 | -44.1497 | 2026-09-28 18:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 8b3dcc57-c0de-3cc6-861c-eff31a6de664 | -7.4185 | -55.6301 | 2026-09-28 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 97c62580-a326-3711-b190-85283aa6c46d | -12.6878 | -45.0192 | 2026-09-28 18:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 02d7005a-ac8d-370d-8ac1-a5251336f26f | -12.6267 | -47.2851 | 2026-09-28 18:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 256.8 |
| db2beeb3-361d-381d-baaa-7572f1e796c4 | -12.6263 | -47.3075 | 2026-09-28 18:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6343ae02-5a09-3f8e-94f5-9253f2fd990c | -11.1775 | -44.7832 | 2026-09-28 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 373.5 |
| c09cd7dc-d58e-3d0c-b1e0-c19a87b1627e | -10.8967 | -50.6866 | 2026-09-28 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 551cf82f-2e14-3571-a6fa-139f3b290177 | -8.2992 | -54.7348 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 972dc2d4-3957-35be-8975-f23ef4a4e9d8 | -7.6903 | -44.8761 | 2026-09-28 18:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 573cf06b-668c-3d59-8731-7f88153e8274 | -11.2753 | -43.5539 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 74a16958-71a8-3674-9b66-2cec3262b8f6 | -11.1966 | -44.7805 | 2026-09-28 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 543a2066-5649-36bd-baea-990543b41118 | -9.9396 | -50.2304 | 2026-09-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 01d76437-5af2-330e-a101-0e784c07f89e | -9.7464 | -53.8784 | 2026-09-28 18:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 4f72e16f-84d5-3816-98e1-8a30833e8ec0 | -8.7267 | -44.8836 | 2026-09-28 18:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c91b0f87-89a7-3c81-9b8e-af0d587790a3 | -15.112 | -53.8838 | 2026-09-28 18:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| f26a145f-3445-367b-854f-308485cccd24 | -12.5043 | -49.9858 | 2026-09-28 18:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ad4b0e68-c735-3b40-87f6-9ac933605201 | -10.6869 | -44.4576 | 2026-09-28 18:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 29aff1a4-1461-3e5c-9a6d-c01fc2c20b51 | -12.2301 | -50.4288 | 2026-09-28 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8ed7b5ad-1df5-307f-a005-3e1cdf1a428c | -10.7916 | -48.7377 | 2026-09-28 18:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| c698b9a2-2195-3312-9980-eecae1ca6eb7 | -14.0911 | -46.3326 | 2026-09-28 18:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 8ea96fe0-0177-3d16-b5cc-a702321ea4a5 | -11.6213 | -46.7742 | 2026-09-28 18:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 7336c9d9-cd08-3fab-92eb-fb467021b679 | -11.6209 | -46.7967 | 2026-09-28 18:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 611b284a-ed98-3801-b561-46e85df153db | -9.9781 | -50.1626 | 2026-09-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 370ebea0-b4ae-3229-85e1-7fa0cae162be | -14.0915 | -46.3096 | 2026-09-28 18:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 456.6 |
| 86f92856-174f-33e0-b485-6e3d51311600 | -11.6986 | -43.4654 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ffde7f91-58e0-325c-9866-843fcf14b89e | -10.6505 | -50.7123 | 2026-09-28 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 20c5b0fe-b8f7-3763-b191-b79ee9a9e626 | -11.6981 | -43.4891 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0ecd69d7-9fab-3872-af92-644c9a99d1ab | -12.1202 | -57.1767 | 2026-09-28 18:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 3d652c32-03e8-3f94-80ee-cc1c8dea2bad | -11.2758 | -43.5303 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 2d226efc-035a-3e68-9194-f2095653e6f6 | -7.3175 | -44.591 | 2026-09-28 18:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 34a20e3d-72ef-3a96-8bca-3a69bd801660 | -10.0148 | -50.2443 | 2026-09-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 90d11cd8-c959-34d0-ae5a-14b31d4861ea | -9.9393 | -50.2518 | 2026-09-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 183f9af4-c78f-3c07-9b54-2fa5d11a3d78 | -12.6447 | -47.3497 | 2026-09-28 18:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ff00ee1d-8618-3293-a876-f8ef5ef20334 | -10.1095 | -50.2135 | 2026-09-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6ac4eda1-ed64-3bd6-b3e5-6e37dbb1fc2e | -12.8513 | -50.9957 | 2026-09-28 18:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 2f5a6ec1-64a4-3929-9a82-81f3d2b67283 | -12.6071 | -51.9595 | 2026-09-28 18:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 048da096-140d-3753-a404-2a1c9bb5b655 | -12.1547 | -50.3735 | 2026-09-28 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 14038e81-e9c4-3708-86d4-a29e72eef16d | -10.8191 | -57.1795 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 256.3 |
| 367f84db-0cb3-3f90-899e-512c416298c3 | -11.983 | -57.6066 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 01c46e95-d2e1-3304-afe5-af5b0a3edd5f | -9.7684 | -44.8312 | 2026-09-28 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1f19eea0-d1e6-3cd6-bb9c-5e8e95af0974 | -10.8373 | -61.3988 | 2026-09-28 18:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 78747dbd-d35c-3827-91a4-06af61f8d08c | -8.1871 | -54.7824 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| f820608e-e616-34fb-ade2-7dc66a046d9d | -7.4974 | -55.0256 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 238.1 |
| 9b97d293-36c7-3aa3-8d89-a8fe7c7ab525 | -10.9349 | -50.6612 | 2026-09-28 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f9f8434e-3201-3592-bac3-f941e697f134 | -8.2623 | -54.6969 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 6c96bf60-3cee-3c50-b1db-0b38b91865a7 | -11.3436 | -54.1086 | 2026-09-28 18:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| f66e1be2-a56f-33cf-9875-8958a03dc397 | -10.824 | -60.7246 | 2026-09-28 18:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 89a45a91-7f26-3c93-9d5c-774e76c6c14d | -13.3272 | -43.9285 | 2026-09-28 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 6e500157-f360-3f89-bb83-83f95d036cbb | -10.8184 | -61.4191 | 2026-09-28 18:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| ba91d834-06e8-38c9-afc4-c9dbb49263e3 | -10.5349 | -57.4382 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 75752141-fcc6-3a6c-9749-220bd36275eb | -11.6096 | -44.1382 | 2026-09-28 18:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 235.2 |
| c30ce1e6-9a2e-3c04-926b-81f2fd3d51fa | -9.9784 | -50.1412 | 2026-09-28 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| bb41aaa5-e4b6-3bb1-ab39-a43eeac89567 | -9.4535 | -41.8088 | 2026-09-28 18:20:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 182.7 |
| da0f3f7c-727e-3389-9088-28fb05b80f2d | -13.3641 | -44.0166 | 2026-09-28 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| cb441de5-741d-34aa-ad98-a4080039ba81 | -11.6994 | -43.4178 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| d2220c1a-b9c6-343a-9248-62c402437539 | -6.314 | -43.5946 | 2026-09-28 18:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ca10e56e-2b55-37a5-ab55-35bdeb69f57c | -11.2566 | -43.5331 | 2026-09-28 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 53b36489-e1fa-39c8-8031-609a03dc6ef7 | -8.2807 | -54.7158 | 2026-09-28 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 6841138e-9e65-341b-8ef4-7e1a7147da10 | -12.6271 | -47.2626 | 2026-09-28 18:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 9dc6f524-f5c7-37b8-9f08-b3ae2992512d | -8.2291 | -45.4602 | 2026-09-28 18:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 278.1 |
| de8a6dbc-fc45-3ea5-b81b-baa53c655bd4 | -10.9538 | -50.6592 | 2026-09-28 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 446be962-a2ea-3608-b8f2-290acba20692 | -13.384 | -43.9895 | 2026-09-28 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d474fdd5-fed3-3637-baf3-f4e89681eea4 | -10.8001 | -57.2007 | 2026-09-28 18:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 6ae5cd4b-cd89-3b93-a2e6-85972e147878 | -6.3137 | -43.6178 | 2026-09-28 18:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e9b6dfc2-d566-328b-98be-007ad2cbd525 | -12.6832 | -47.3442 | 2026-09-28 18:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5407bcd1-b5fb-3295-9818-e912cde8e59b | -11.1775 | -44.7832 | 2026-09-28 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| cd2f938f-7ed0-385b-b775-a86f6b2892ce | 1.6566 | -55.903 | 2026-09-28 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 93f5fe0f-d8dc-31d7-8395-69669a972ee0 | -9.9393 | -50.2518 | 2026-09-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 906ae6d0-0dcc-3f87-bc53-222878635493 | -11.1962 | -44.8037 | 2026-09-28 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |


[Clique aqui para ver as próximas entradas](README174.md)
