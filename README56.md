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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4750a383-e0da-3068-890f-f661c4213cdd | -10.7434 | -50.8302 | 2026-09-27 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a650eafe-127a-3b48-84e2-21c4758c74ae | -11.9586 | -50.7393 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 0da64a5e-c989-3c92-9db1-494bb2937648 | -12.2311 | -50.3643 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 91613831-6248-3cec-bc7b-0d670c93aad2 | -6.8594 | -43.5237 | 2026-09-27 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 981273c0-9eb6-344f-9be3-9ae8d93f040f | -5.8496 | -45.168 | 2026-09-27 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 455b2328-6847-37ec-a2d3-7faf25f33fa4 | -12.2639 | -50.7034 | 2026-09-27 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d722a37a-2d22-368c-9027-14eb0cdf19d1 | -12.7221 | -47.3161 | 2026-09-27 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 824d7899-c771-31aa-84dd-f3f10ea54968 | -11.9845 | -50.2864 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2b801373-6ece-3a43-b76c-af9db704a937 | -11.809 | -50.5642 | 2026-09-27 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c7573bc2-da09-3cae-ba25-40ce5477c971 | -12.0369 | -50.6019 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1a1ac1a5-c574-3fc1-b3bb-19cc4fe42d95 | -12.2643 | -50.682 | 2026-09-27 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| fa5348a8-c250-30ea-9e10-691be34aca9d | -6.8408 | -43.5021 | 2026-09-27 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 225.0 |
| fb92025d-8e23-3c7b-b3c9-d8d46e45145b | -11.9845 | -50.2864 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 53f6fdee-fb50-35dc-b61e-701f39a16dce | -17.0533 | -56.5693 | 2026-09-27 13:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 6e59c52e-d340-3e1d-979f-568d513321bf | -11.803 | -50.9704 | 2026-09-27 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 57406e89-c9e9-31fa-9889-c60ab47ae911 | -12.0615 | -50.2343 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4415127b-1c31-342b-a753-739ee36dfed1 | -7.055 | -42.849 | 2026-09-27 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| d19585ce-e0c5-3795-9e54-987a1aa0134a | -12.2639 | -50.7034 | 2026-09-27 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 12096e8c-ad31-357e-b581-ea772241bcf8 | -12.2498 | -50.3835 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c85e658e-7d2e-32d1-8ad2-e09e946b8be7 | -12.2834 | -50.6797 | 2026-09-27 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 45cf91c3-d151-3c4b-8688-cb1319302f03 | -6.8405 | -43.5254 | 2026-09-27 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 634b5f9d-0a2f-3637-b069-c63d6824fef0 | -11.0233 | -54.0559 | 2026-09-27 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9d6a0c57-0bd0-3ac6-93b6-cf843456c0bf | -12.1175 | -50.3135 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 63b16e39-fa69-3d4d-abb0-4be595312845 | -7.2102 | -39.3549 | 2026-09-27 13:10:00 | GOES-19 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 9d51ba16-755e-377f-919f-81d5c87d02c7 | -12.0178 | -50.6041 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 87c6d678-0efa-30a8-99e6-e929bcc867d2 | -12.2448 | -50.7057 | 2026-09-27 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d4ba2556-1130-3ed6-acae-b5c2092640d7 | -12.0806 | -50.232 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 85f5561f-d196-3fa3-8d4f-712daaf8cc0d | -10.0159 | -50.1588 | 2026-09-27 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d9b43f4d-37fb-30ee-86c2-9ffe9f51eb11 | -12.0181 | -50.5827 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 21b1850b-eecb-32ab-a76c-0b76d5da9f2c | -12.2257 | -50.7079 | 2026-09-27 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cafd2d89-e3d4-3c28-b419-6be55cea9446 | -11.6009 | -50.5025 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 37202a66-6233-3d75-8971-2ca8994f5781 | -10.0162 | -50.1374 | 2026-09-27 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 24834fba-68b1-3542-a786-fc945b84e6a2 | -11.0619 | -52.4812 | 2026-09-27 13:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| fdb96d8d-fffe-3fac-842a-a6e0268e632b | -12.2311 | -50.3643 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e89b86e6-c1a7-3258-8d3b-52e3043e4309 | -9.8427 | -44.937 | 2026-09-27 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0fe1d95e-8d56-3649-befe-39d27248125d | -12.2307 | -50.3858 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 8a7382dc-b974-3e7c-9483-b7eeb092c012 | -12.2502 | -50.362 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 066f124e-4e97-35ab-8232-a94d38f92e43 | -7.3653 | -42.1058 | 2026-09-27 13:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 5e2695a5-3226-3e83-b3f5-a6dd43870193 | -11.7834 | -51.0152 | 2026-09-27 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1a31b207-f585-3351-9fb3-eeed2122c9ce | -12.1171 | -50.335 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d87f80ef-c0e2-3ab3-a1cf-805b26e8d7c4 | -11.0235 | -54.0354 | 2026-09-27 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b9fd60e1-3bb8-34dc-a29e-06ec197cd30e | -7.365 | -42.1298 | 2026-09-27 13:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 58565b89-1c68-3b71-94af-4ae4b5ae85c0 | -12.1362 | -50.3328 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 34fefec6-0442-3797-8ddf-616a4be806b0 | -11.6199 | -50.5004 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b2ac6c40-bb7a-33f0-8755-ce177598365c | -11.7831 | -51.0365 | 2026-09-27 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 08271ec5-63dd-3c5c-936a-3cc064fd4aab | -12.1366 | -50.3112 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 19b7014e-b53e-3ea0-81be-2b4f14dbdaf8 | -11.8027 | -50.9917 | 2026-09-27 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 00f4bac3-a503-34f0-b6a5-8632b66f18e7 | -11.5818 | -50.5047 | 2026-09-27 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4a48cd6c-6142-3781-9675-c6ad835190e7 | -6.8596 | -43.5003 | 2026-09-27 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 79c723d7-b540-393f-93db-c2cc6f3d7d50 | -12.1106 | -50.7643 | 2026-09-27 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4e523b01-c2da-37aa-a9e5-ec8acfb70241 | -7.055 | -42.849 | 2026-09-27 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| e87ff7c4-9e09-3533-873a-1bb4802adb4c | -12.1366 | -50.3112 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 55914528-2cbd-3b0d-a141-f743f3ed1c51 | -12.1109 | -50.7429 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4aafcc43-3089-330d-a847-8cb956dc8370 | -12.2257 | -50.7079 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ffb6a433-f476-3233-b895-1a7a1d984c2d | -11.0233 | -54.0559 | 2026-09-27 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b04f7cc0-d13f-3f11-99bb-ee57e34f2dda | -12.2502 | -50.362 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fd648410-6527-35a4-9c05-e96d5abd93cb | -14.13 | -46.326 | 2026-09-27 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 254de69d-fdb3-35e7-b6b2-6b69a045deb6 | -12.0806 | -50.232 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7ea14dbf-ccd7-3a9e-b36f-44f61b01ebca | -12.4351 | -44.1497 | 2026-09-27 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 382.0 |
| 53ec087b-91c0-358e-8e73-5e05d7222d45 | -12.1175 | -50.3135 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6a353d43-40b3-3f6a-8017-ca6d7b46850d | -12.2643 | -50.682 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1bd37d9c-2f2a-328b-8798-51aa3cbe8d8f | -12.2311 | -50.3643 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ecb42071-0463-3192-8e0c-09844f05fd05 | -12.0605 | -50.2989 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4ad27f56-2583-3cbd-9a2b-6d31a1517e85 | -12.4355 | -44.1262 | 2026-09-27 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 194.7 |
| eda145b1-0002-39ba-a920-c465d6e46eba | -12.6647 | -47.302 | 2026-09-27 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ab02121d-156f-36b1-b47a-635009430b80 | -12.1106 | -50.7643 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| df6c4dfa-162e-3257-a0c9-5db9a8b1fea0 | -9.9318 | -49.3733 | 2026-09-27 13:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 4003e924-dc65-3b0c-8fc7-a679ded42fbc | -6.8408 | -43.5021 | 2026-09-27 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 494e9841-e802-3e9c-8383-6f80be045daf | -12.1362 | -50.3328 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| fcb6b1c0-4d54-3593-8304-dbdfd4d692aa | -7.365 | -42.1298 | 2026-09-27 13:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 165.6 |
| 04d6582d-1488-39b2-b8a1-af9b5881beb6 | -12.0178 | -50.6041 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8ad3e586-43e4-3307-9e09-6cb9e2c0f145 | -11.0235 | -54.0354 | 2026-09-27 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a7977a53-0ce0-3e4e-b73f-ba187d2fe575 | -12.13 | -50.7407 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 22e78052-2156-3760-81a3-7f51c12018ff | -11.0619 | -52.4812 | 2026-09-27 13:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f978bcf3-e9ac-366c-b3e1-5539be7b9532 | -6.8596 | -43.5003 | 2026-09-27 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7803ba29-a730-3f84-9bd1-39809057372f | -7.3653 | -42.1058 | 2026-09-27 13:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 174.2 |
| 7d073128-836f-342e-9037-bccf3f826e9f | -12.2448 | -50.7057 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| fa14d43e-449e-31f2-b042-d1b51686c2a5 | -17.0533 | -56.5693 | 2026-09-27 13:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 11666822-83e5-30bd-a46c-529a42a742fa | -12.4157 | -44.1529 | 2026-09-27 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 292.1 |
| 7ee9090c-7ed0-3fd2-996e-fbb7e5490e4e | -12.2307 | -50.3858 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a48f2c4d-4366-342b-9b4c-a2ebc91c5f2a | -12.2498 | -50.3835 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1495bf01-4ccc-3b6a-bd3c-6adea29e4488 | -12.1171 | -50.335 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2f78ffbd-51c2-33a1-827f-6770db27d8a7 | -9.8427 | -44.937 | 2026-09-27 13:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| bc11fc29-1925-3986-b074-460335eaa17a | -6.8405 | -43.5254 | 2026-09-27 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| fd1ca914-5fd4-3175-9a16-0b88640cc2e2 | -12.0609 | -50.2773 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| be366fd2-3dbf-340c-875f-6fc390428a97 | -12.2639 | -50.7034 | 2026-09-27 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0a5a257e-6978-37f9-9ca8-86330134d108 | -7.3842 | -42.1039 | 2026-09-27 13:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 274b07f2-c1d6-35ea-b279-245df8b37059 | -12.0414 | -50.3011 | 2026-09-27 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 38569dd4-8b2a-357a-b0d8-5901507fcfaf | -9.04501 | -66.04422 | 2026-09-27 13:21:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 08c6df59-4f87-3fcc-b274-17c89ffb0b6d | -4.09865 | -63.28631 | 2026-09-27 13:21:00 | TERRA_M-T | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f020795a-17ce-3640-bfcd-49dc1330e1e4 | -9.05044 | -66.1041 | 2026-09-27 13:21:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 20515007-a518-3793-a9ef-ee76b7b157c8 | -6.8408 | -43.5021 | 2026-09-27 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 9ce6f65f-eb80-3f40-8e0b-e998b1efddf7 | -9.9318 | -49.3733 | 2026-09-27 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b237516a-06b0-3e5f-8222-83effc132877 | -12.1369 | -50.2897 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4cce4132-4ce2-3d4c-a7c7-f908ad027417 | -12.4157 | -44.1529 | 2026-09-27 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 271.2 |
| 484d9cb5-927d-38ec-8824-74d9c1329fb9 | -12.4351 | -44.1497 | 2026-09-27 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 926ceae6-0444-31f0-9e56-3aebbeab7073 | -12.2502 | -50.362 | 2026-09-27 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f769084f-bd0a-3bda-9b93-3f996d17cb7f | -11.0619 | -52.4812 | 2026-09-27 13:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 18ce3017-9131-33da-b38f-9bcdd2a06a38 | -14.13 | -46.326 | 2026-09-27 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 131.1 |
| b33ebabb-333a-32eb-abf7-54bcac741df5 | -17.5697 | -46.9019 | 2026-09-27 13:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |


[Clique aqui para ver as próximas entradas](README57.md)
