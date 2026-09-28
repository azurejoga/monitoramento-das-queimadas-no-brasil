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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cf49bac-30bb-3cc4-8c0c-50c4e76b7197 | -11.0424 | -54.0336 | 2026-09-28 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7ff48e22-1e76-369e-8586-0979aadf70fe | -12.2251 | -50.7508 | 2026-09-28 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a74559c1-06bf-37e7-991e-83478db39c46 | -11.3043 | -51.3434 | 2026-09-28 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 366e350d-35ef-3816-9140-30362f15cb9d | -11.0991 | -54.0285 | 2026-09-28 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 358ca2c6-814d-3e38-8fbf-8f033a9df52a | 2.1082 | -50.8583 | 2026-09-28 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 62229cd8-26bc-3a4d-a646-81acf858f511 | -15.4199 | -47.9001 | 2026-09-28 17:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 152f0634-e93e-332d-a754-f0a9182acfc3 | -11.8427 | -50.8594 | 2026-09-28 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 8c07a927-99df-3659-97e0-d7ab949251e6 | -11.0991 | -51.1111 | 2026-09-28 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 65138b54-38e4-35c8-b1c3-e166c4a517fe | -12.1737 | -50.3712 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 17f5ecca-caa5-3b03-9713-6706d4465edc | -12.1731 | -50.4142 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 210b8163-991f-3c34-b56c-120c7378fd89 | -11.0767 | -51.3674 | 2026-09-28 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 83901323-c81d-3029-9fb1-59cf6ddef57d | -9.7874 | -44.8289 | 2026-09-28 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5283ca01-517a-356c-afc0-cbfd1f92aaad | -9.9784 | -50.1412 | 2026-09-28 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 0383593f-6df3-38de-ae59-5e5e1cfe0fea | -15.4003 | -47.9035 | 2026-09-28 17:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| abc1f2bd-f3a5-3a74-b48e-29e5c6cb5370 | -15.6565 | -52.694 | 2026-09-28 17:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 39f82333-bcd8-34eb-92c3-e86ce71bc0fc | -15.0984 | -54.7189 | 2026-09-28 17:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| bde16425-b489-325a-898b-1ffa89cf5af0 | -9.9781 | -50.1626 | 2026-09-28 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d37d0cef-96da-3da2-aa20-e47354bee406 | -11.7647 | -50.996 | 2026-09-28 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4c8be5a4-5eba-3993-b1e4-7fa4053f8623 | -10.7434 | -50.8302 | 2026-09-28 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| c55787a6-3ba0-3e95-9f1c-bb0c018afb12 | -10.8967 | -50.6866 | 2026-09-28 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f5cc1166-227e-3567-ad5d-22cec65bb9c1 | -11.1775 | -44.7832 | 2026-09-28 17:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1074.9 |
| 808d4a2c-a214-3480-ba1a-d8637bbeb48b | -12.1359 | -50.3543 | 2026-09-28 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 4421ea49-feb9-3bc8-ad45-d11c581f91ef | -9.7874 | -44.8289 | 2026-09-28 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| cf51f305-0a14-37b3-a8ff-1f5618a98707 | -10.0159 | -50.1588 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 0b0d5234-7312-38b9-9992-ec593bc3bc8d | -10.6035 | -49.9913 | 2026-09-28 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| eac67d5f-2772-31a8-be62-07028b3acf5b | -10.2446 | -49.986 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e2bea18d-2406-3048-b39d-cdd08d08bb53 | -11.9777 | -50.7371 | 2026-09-28 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 35994fb9-d58f-3782-85f0-b55ad455104d | -9.9773 | -50.2267 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 99aca936-c379-32c1-bf38-866a3534c1e5 | -10.2827 | -49.9606 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a24e5318-1f37-383d-8e8e-dd642748a4fc | -10.2067 | -49.9898 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 86684ea5-6e3c-3d94-8180-64aea78c2b27 | -10.6889 | -50.6658 | 2026-09-28 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 007a1fde-ea5e-31ac-a770-087e4635f19c | -10.824 | -60.7246 | 2026-09-28 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 76fe2003-5355-3ed6-bf43-bf0921b51245 | -10.2257 | -49.9879 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 7c5c2aa4-2c3a-3aba-8a80-5e1c4f5b48a6 | -1.4116 | -49.0384 | 2026-09-28 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 963bbfb5-6e12-3f8a-8c72-cb99154d34bf | -11.058 | -51.3482 | 2026-09-28 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7996f769-ce92-376a-b98b-df33fe51455e | -10.8052 | -60.7257 | 2026-09-28 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 19d952ec-27ad-370f-a10f-30eb91f8e829 | -10.2824 | -49.9821 | 2026-09-28 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 503830a1-8543-3163-8252-103a4ad63a1f | -10.6928 | -60.7322 | 2026-09-28 17:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 715625eb-4b94-3745-ad4a-3070be715fb6 | -10.9445 | -43.8849 | 2026-09-28 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 606.2 |
| 26e46733-34dc-32e2-a924-8cf1a5718f1d | -10.6505 | -50.7123 | 2026-09-28 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bffa1275-f40f-32f0-b67e-a9fd96047024 | -1.3008 | -49.0613 | 2026-09-28 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| fc0d7b2b-5215-377d-a154-6cd33d882fa2 | -11.2154 | -44.801 | 2026-09-28 17:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e1172383-cd16-3e1e-b0e1-42868b0167c5 | -8.3608 | -45.4695 | 2026-09-28 17:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2f6e5f5c-d99d-324e-83b5-240165b7aff6 | -11.1966 | -44.7805 | 2026-09-28 17:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 58e4ebbe-30bd-3518-b7a1-564c2c5394dd | -1.4301 | -49.0382 | 2026-09-28 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ffc45447-859b-31d1-949f-2bfef1b250ed | -11.0241 | -49.7088 | 2026-09-28 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 1bea8dfa-2919-3909-88f0-2c5e5171e155 | -12.1362 | -50.3328 | 2026-09-28 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 06a76ea8-fa54-3ab8-b9a3-18f6bd09b04c | -12.1731 | -50.4142 | 2026-09-28 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 63c05aa8-281b-3bf0-86aa-35c1f2f24661 | -11.6404 | -43.4981 | 2026-09-28 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 296.2 |
| 3391f67c-ddd8-34ac-ac86-af1dba281d8e | -8.6169 | -54.6328 | 2026-09-28 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| fa58547f-fa4a-376b-837d-2d5064c9da57 | -10.7115 | -60.7312 | 2026-09-28 17:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 1c91f6f6-85e4-33e0-93ce-7d1e5bce01f5 | -11.6986 | -43.4654 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 0c5c4907-2372-3c21-8a06-6befa2f50ccf | -11.983 | -57.6066 | 2026-09-28 17:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a7e9bb9f-7ae0-3e08-8540-53d9e7290737 | -12.1547 | -50.3735 | 2026-09-28 17:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ac602833-68be-301b-bd74-2adcbada0d91 | -9.9393 | -50.2518 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 1226c67c-e354-30a0-92ba-a375da8b7724 | -11.0991 | -51.1111 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ec412260-de0a-3a5a-91c8-31eebf629682 | -10.9449 | -43.8614 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 15295ee2-dc70-35d5-842a-808d11485085 | -9.9976 | -50.1179 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 752486cd-300c-3fcb-9db2-af59eb9c2b11 | -9.0969 | -49.9049 | 2026-09-28 17:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a15d0edb-a428-38d3-b837-c56ae4d36345 | -13.161 | -48.5437 | 2026-09-28 17:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ee60e629-9199-301a-a0bb-f3e5ce78a7c3 | -10.6094 | -53.9902 | 2026-09-28 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c00ff4f4-43b9-3f12-a102-c8eeef4593ad | -11.1331 | -50.0409 | 2026-09-28 17:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| dcdc8f23-a79e-30ff-b9f1-ec5af7cea190 | -11.7828 | -51.0578 | 2026-09-28 17:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8e526c97-a1a2-3089-a723-659a9102cd93 | -13.6866 | -56.6131 | 2026-09-28 17:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| da6098b8-a3d7-3662-b392-dbe5734ef3ca | -8.1681 | -54.8239 | 2026-09-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| c523f6e0-4946-3236-9d94-ed72bfabdbc5 | -10.1286 | -50.1902 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| bba61d38-7703-3ee7-9e4b-7a765e0c7456 | -11.3735 | -43.4209 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.5 |
| e2a5fa96-1263-3f12-89e7-69c154fd3d7e | -9.9784 | -50.1412 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 51e6200a-177b-30df-8c0a-c417b4e3a16c | -10.9536 | -50.6805 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 31235263-6cc2-331f-a259-cd6c2b7925a0 | -9.7874 | -44.8289 | 2026-09-28 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 02bcb371-35d7-3ee3-9595-ccdad82eb735 | -12.1075 | -45.2248 | 2026-09-28 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 78ff36f6-162f-3754-b710-8879fe8667f7 | -9.9781 | -50.1626 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3d056466-de1a-3961-8f1d-0ff0a3a5e766 | -12.7417 | -47.2909 | 2026-09-28 17:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| ee500358-b6d7-3a6f-a3b7-74cc794f851e | -11.6213 | -46.7742 | 2026-09-28 17:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c860c1e6-6055-364f-879e-66ac7e5d400d | -11.6209 | -46.7967 | 2026-09-28 17:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 750d1de1-32d6-39bd-b40a-640b13b771e2 | -7.6903 | -44.8761 | 2026-09-28 17:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 0b9afcfb-0df5-3b11-a9b0-456150ef1a65 | -10.8967 | -50.6866 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 80f28cfc-e5d9-358f-b2e1-8fb8ba6f2092 | -12.4351 | -44.1497 | 2026-09-28 17:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 882f3f44-791e-3510-8d14-a16bdc8c3666 | -8.6169 | -54.6328 | 2026-09-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 4a1efba1-8a95-3710-8167-995debed4f3e | -11.2758 | -43.5303 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 5905faff-f3e9-34ba-9f76-a413df6b2079 | -10.7434 | -50.8302 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| eed4f241-8470-3a86-a8c5-31553f5ca0f1 | -11.1181 | -51.1091 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| f4825d80-113a-3e71-be06-45a2050b72a4 | -10.5957 | -50.569 | 2026-09-28 17:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1428c84e-2be0-38d3-ab00-87f27b074926 | -8.8735 | -49.7328 | 2026-09-28 17:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 97688004-4c53-38e9-91c7-1f912e7bab6b | -11.2753 | -43.5539 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| b8306f46-3b92-34fd-bb21-072afcbe00b7 | -10.6928 | -60.7322 | 2026-09-28 17:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 7251bc52-d790-3974-985b-5515587f7f8f | -15.4003 | -47.9035 | 2026-09-28 17:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0508d098-73b4-3dd8-a0ce-1c2e69c87a8b | -12.9457 | -51.0695 | 2026-09-28 17:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 1a7a43bb-71a5-358a-bf3e-296f23d78028 | -10.6505 | -50.7123 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f11a1795-abe3-3592-bbca-54d295f5fb6b | -15.2699 | -47.61 | 2026-09-28 17:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c7353ff6-65e5-3b23-9df2-4b6c97c63913 | -15.2694 | -47.6327 | 2026-09-28 17:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 2badff95-5e82-3dbe-acff-b3009e65b781 | -10.6869 | -44.4576 | 2026-09-28 17:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a8381bcd-99f7-3cdf-b650-a1165a4768a8 | -8.2807 | -54.7158 | 2026-09-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 221.0 |
| 5c893e0e-0e2b-32fb-83a4-ad66e0a210b6 | -10.9349 | -50.6612 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6ca03bd6-7998-3d33-a990-94c2d8e515e3 | -8.2804 | -54.7562 | 2026-09-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| a1ef0421-8cd9-3e17-bfd1-08eb415517f3 | -11.2154 | -44.801 | 2026-09-28 17:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d57b3afe-5853-3d4d-82c5-64f520e8331e | -10.9538 | -50.6592 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 3ebd5099-4880-3dcb-8ddd-c96377e6bc46 | -9.7684 | -44.8312 | 2026-09-28 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 6410b7bc-0701-3fc8-8039-b60dd4a95ff4 | -12.6071 | -51.9595 | 2026-09-28 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a94b6cfa-e2e2-323c-9416-f35d1ed6a427 | -8.206 | -54.7408 | 2026-09-28 17:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |


[Clique aqui para ver as próximas entradas](README171.md)
