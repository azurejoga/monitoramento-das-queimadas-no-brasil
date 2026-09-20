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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7628f7e4-4a6b-3c63-a796-614d538fa922 | -13.03493 | -46.92088 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bef364b5-7b84-31fd-9700-f490e02cd34f | -7.15504 | -47.46038 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba3feda9-3ca4-3d85-92b7-04d6d123f609 | -8.66672 | -45.4348 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb8e3780-b21f-35c3-b0ee-ebf002295eaa | -11.47849 | -47.73546 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 729f78af-0c5e-3daa-a9b6-add42abee6dd | -11.44503 | -45.33073 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c840e718-f0f4-3264-a162-566c6f29c9da | -12.34315 | -50.68944 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17292ac0-533a-3646-b91c-d4a47f112ed6 | -12.7569 | -46.21531 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38f966e-b2e4-3ac8-8a93-6153d5d21421 | -11.00483 | -48.31163 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6309d5eb-8efc-3a8d-8708-16dc65c42ac1 | -11.83766 | -46.85116 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01b7309e-9bc9-3df8-bf3b-0427367372c4 | -8.45239 | -45.86814 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c8cb861-4ddd-3fd1-9120-b14d00e48357 | -6.88908 | -42.92854 | 2026-09-20 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 41770417-9f80-3bc5-be31-884be8f815fe | -9.04855 | -48.72628 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 27b132ed-c351-3637-9324-7ecde0c1e3c0 | -8.9965 | -45.00714 | 2026-09-20 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5fbc4d1-1565-31a0-983e-b8f790c82d3e | -9.78679 | -45.06671 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6600a687-eb82-34ce-98b6-da69797aecde | -11.84508 | -46.87261 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 928a839e-f2fe-3c8a-b31c-ad6ba32e0cdb | -7.96811 | -44.07663 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bd73eb5-2f98-314f-b38d-7e4f908cf06b | -11.86195 | -47.66763 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9feb9443-d053-3949-ac1c-2e3022e65397 | -8.44761 | -45.86256 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19280806-53eb-3e8d-ae1a-aa055f38ce74 | -13.01876 | -46.91542 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2056d506-b41c-3ef7-b7a2-a3a1989c160a | -9.83474 | -46.44269 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 59b210aa-6b09-367b-bcfd-49abd9348667 | -9.81795 | -46.4382 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62c6b112-2cfd-3e98-b53c-da2a1f4b86f2 | -12.13352 | -47.02779 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1b5829f6-84bc-3a28-9202-eb0059988c0f | -8.87296 | -45.95124 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3630fc0c-9036-3e46-bdaa-46ebc4d17ac1 | -6.51518 | -46.77879 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 19845283-5458-3c6a-86b8-676579dbae8f | -9.54519 | -45.40574 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ea40715-ce72-35c1-a06e-f008bbaad4ca | -9.12853 | -45.71207 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b82ae36-9c39-390c-acc3-645ed2629075 | -11.45349 | -45.3709 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe59eb41-90c0-379d-9a04-548d49433926 | -7.55096 | -45.44719 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 220357e7-6abf-3378-8a6e-bc92bf8ea430 | -11.15069 | -42.79851 | 2026-09-20 03:45:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07d51d15-c17c-3160-9d7f-2ad1a4579c27 | -9.54581 | -45.4024 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acfc80a9-ac30-3761-b068-24995c3c447a | -9.263 | -48.21111 | 2026-09-20 03:45:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fae038ba-f14f-3f83-a77f-280157897e3b | -10.54731 | -46.73686 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bcdc54c-7c5d-38ef-93a6-ed00ce1d6a18 | -13.03367 | -46.92391 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| beb1e7a2-3a8e-3ac3-adde-6d2092d249eb | -12.75743 | -46.12856 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cf8233f-ceb1-3284-9b2d-501a2a219e00 | -10.78312 | -46.32948 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbc88b82-de70-322b-b782-33fefe45bdd0 | -7.57621 | -44.90172 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04cdae40-0549-3b4d-ad92-844d0b66692e | -7.41805 | -44.70173 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 746ea7a7-8bfd-3e7e-8268-4bc103074a6b | -11.09177 | -48.28658 | 2026-09-20 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4460899c-ad72-383e-b49e-caf2a9113415 | -10.86082 | -50.17959 | 2026-09-20 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e18155f-29ee-328a-afdc-e7da4e943ce5 | -11.85979 | -46.87158 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1c70fa3c-a632-3664-98bb-98d2d98daa43 | -11.86702 | -47.67313 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8d41771-2c2f-369a-85bd-0ea46cceb940 | -10.60474 | -46.52587 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18d2da0d-1e9c-3ed0-8a12-0fef2723de80 | -6.56243 | -45.58326 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 035dfc9f-7527-31b9-9c14-29e3b3ff133b | -9.78621 | -45.06989 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad2e230e-c8b2-3c81-95de-43c20fd6a740 | -13.0237 | -46.91634 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b854a6c-fb19-3d9e-a644-1d18d7a0b049 | -6.30104 | -47.62051 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0926461b-4513-3ffb-94cb-e55519e0d013 | -9.70874 | -45.86867 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bba063f3-7393-342e-a64a-3e193ed529a4 | -6.30386 | -47.60487 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d697d552-0f03-3e24-b873-24001b5ed7c8 | -9.35971 | -40.31183 | 2026-09-20 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 5723f7a6-ef83-3779-994d-4674253de28a | -13.01959 | -46.90818 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 361ac893-f6ae-3e5c-9843-830cacfcb961 | -10.12498 | -45.55567 | 2026-09-20 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77c31334-96d2-3f25-b712-c1ea5ac0026a | -12.36996 | -45.80532 | 2026-09-20 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00cb9ee8-25a4-3306-8fd9-015aa704b06e | -9.26097 | -46.20028 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01b98ec7-8539-39eb-a21d-592fb41fe4a2 | -5.83382 | -47.78991 | 2026-09-20 03:45:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fcdae40-49ad-301c-96ba-8fe4e19b237c | -12.15786 | -47.02361 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d780aa47-625a-30bf-b8e8-c5c3964f9b0c | -10.55142 | -46.74643 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4148caea-d379-3381-8c9c-c0abded11580 | -12.76275 | -46.12939 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7a927788-c556-3445-8090-6bcba8fe90e5 | -9.26032 | -45.95306 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebb6e7a8-96d2-3c22-b758-5acba6659a07 | -9.12785 | -45.71582 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e2c80d42-95e5-3e53-a4f6-91d41a83657b | -12.15697 | -47.02808 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 227188a3-f025-3a73-81f3-ce5d14234cd7 | -11.45017 | -45.33163 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1503c821-5ddf-3c91-9f23-44efa5c3b86a | -9.54046 | -45.40148 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e5430fa-f9d4-336d-8ee2-acb0e2710247 | -7.97367 | -44.07446 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eea97d91-6303-32e9-af20-95a9db077312 | -7.87739 | -44.85688 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45fef4d7-c8ae-357c-835c-3b772f558495 | -7.51999 | -47.33437 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f2d5b03-75bf-377c-8cff-1bbc070532d2 | -7.87798 | -44.85355 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea59324d-ed20-3603-97e3-c9c54f168087 | -7.55107 | -45.3827 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ffe2472d-3697-3aa0-bcdc-2071139155dc | -7.49527 | -46.71388 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f51e3423-b78d-32f1-86ce-c817733b303b | -10.39202 | -48.99521 | 2026-09-20 03:45:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 665a7800-e172-3087-b3b2-28407db626cd | -6.31919 | -47.63148 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 27ba511e-c562-3a62-9e6e-70a2dbdd5bcf | -8.22002 | -45.6112 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02580096-f27a-313c-abfe-b2789f62dfb6 | -11.23592 | -48.3848 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c0c568c-9c43-3890-ab39-7c4785676f88 | -8.62908 | -47.62399 | 2026-09-20 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf70e500-9d64-3bce-b32a-836a97840371 | -7.43455 | -44.76221 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 454c46c5-e855-3296-a05d-c6f469e26191 | -12.13679 | -47.04082 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64636c3c-fb68-3b64-b667-55e21398febd | -11.77059 | -47.45842 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 673a7c68-f77f-3632-885e-70e16de1e831 | -7.01855 | -45.24712 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 67a7a2b2-f6aa-3c25-a34d-e09c23496420 | -5.84038 | -47.79123 | 2026-09-20 03:45:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa18fae8-ca95-3a74-ae39-0c331810b4f9 | -11.49535 | -47.78721 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da87770f-5d9e-3245-a4cd-245dd896ae8c | -9.82585 | -46.42746 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ac51e70-da42-3892-8da4-1e84bdc7bc2c | -6.64969 | -43.62834 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adfce9ed-ad1e-35d9-a534-234702fab56f | -6.46145 | -48.42666 | 2026-09-20 03:45:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e28f06d4-3e63-3893-978e-783ec0857797 | -6.80035 | -47.81948 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf8437fd-43a7-3ac0-bbc8-962e36c3a12d | -10.49214 | -46.27337 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b507876d-41f6-3fd8-a434-e5eb5bdb151d | -9.82953 | -46.43913 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1851c738-d778-3285-848e-37e9036c3504 | -6.31271 | -47.6304 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 92d31183-e930-325d-a0f6-86ce123f8652 | -7.80207 | -44.94061 | 2026-09-20 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c4decbc-fafe-3ac4-bb8f-1112b454c7d5 | -11.65798 | -43.4288 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 862584c4-a37e-3f72-9a9e-37b3e6e34d72 | -11.87661 | -49.00496 | 2026-09-20 03:45:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6b59cfb-64b0-3bfb-a180-e10eaff84365 | -13.02487 | -46.91356 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f55f1641-fd2b-3162-bf71-f861c7909b3d | -10.29105 | -50.31351 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf2d43ca-9e07-3d29-8960-f3b02e51573b | -11.8394 | -47.62658 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6fbef5c-dece-30a8-8800-3c44c24a9356 | -13.28265 | -46.73043 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76c1eeb6-2c7f-3025-ab65-71dae763c8b4 | -13.01895 | -46.91139 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4daf96da-d091-3d80-bc69-d0a7c5db763e | -6.96703 | -42.58491 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afdf6c6c-f876-3810-b7a6-a3c15605a333 | -6.45161 | -48.44209 | 2026-09-20 03:45:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9cef98ba-1de7-3ba7-bb10-2ce0105c283c | -11.44998 | -45.38972 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 289ea60e-01e1-3933-ac61-7e2d65f56d4e | -7.55716 | -45.44444 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 761eb103-d510-30f6-8e7c-4c527f876a74 | -11.00203 | -46.58839 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f21cb7a-7346-3974-afe4-849dcb058491 | -9.25758 | -45.93695 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README17.md)
