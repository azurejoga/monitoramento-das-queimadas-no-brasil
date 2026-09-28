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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce4f33c5-e665-30b7-92bf-f6cdaf99b52a | -5.7388 | -45.0172 | 2026-09-28 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 3bb5cfd6-7252-3f99-8e01-c93f22be0869 | -11.1324 | -50.0839 | 2026-09-28 19:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f5889875-23ae-364a-826e-fd47fc995865 | -11.6994 | -43.4178 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 9ee126bc-5fb7-3373-b195-2b6608cfe347 | -8.2479 | -45.4583 | 2026-09-28 19:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f93e0a4d-e1f9-33b3-bdce-79b7a912893f | 1.8771 | -55.5646 | 2026-09-28 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cc519de0-d4cb-325c-aedf-ed0a0a555cf4 | -13.3272 | -43.9285 | 2026-09-28 19:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 27168c70-ee69-3815-a326-b4ab11724d89 | -14.0915 | -46.3096 | 2026-09-28 19:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a922eade-e784-38c3-a4ba-892fe2a24dfe | -2.0933 | -49.557 | 2026-09-28 19:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| af00872a-542d-3519-944e-ce0a6ded93d3 | -14.7295 | -45.5527 | 2026-09-28 19:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 1ad78802-541f-37cd-9948-efd5e142a52d | -6.7185 | -55.0684 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 9b964ecc-7b86-3b95-af8b-d077007257ab | -10.8238 | -60.744 | 2026-09-28 19:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 485.3 |
| 24cbcebb-e2e0-378f-9039-3f330b4b4663 | -7.6852 | -54.7532 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| f05cf41d-e4e3-307f-9a22-0b1ce29c0763 | -8.2291 | -45.4602 | 2026-09-28 19:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 738a4a6e-c4c2-31b9-bfe7-f3d3f95d5a3e | -10.1047 | -43.954 | 2026-09-28 19:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 0f07b8fe-c5c6-3b45-8258-dfa4498a811c | -13.3267 | -43.9523 | 2026-09-28 19:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 301.4 |
| fb556109-b2b3-3be2-880b-760f5b16275e | -10.8184 | -61.4191 | 2026-09-28 19:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 2a282b1b-1b92-38c0-a65b-cf31b56af2f0 | -7.5159 | -55.0245 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| d1d78505-7523-3458-8a26-3ef4a775a5f3 | -9.9781 | -50.1626 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 476ce7f5-8baf-37a9-b7c7-2811d4ae27fa | -5.7386 | -45.0399 | 2026-09-28 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 2591f4bb-49cd-32e5-8a28-656c015f908e | -9.1525 | -49.9639 | 2026-09-28 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 8269d194-f13e-36cc-a4ef-6b7b09101c74 | -8.2809 | -54.6957 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| f3cc5238-a070-3ce4-bb90-af61e84d9d7c | 1.6749 | -55.9422 | 2026-09-28 19:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 1814dc3c-1b17-389e-82c6-b018c213b51e | -6.314 | -43.5946 | 2026-09-28 19:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 755968d2-e3fa-3b80-bbef-7b37b02be6b1 | -10.2257 | -49.9879 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 900b0408-9950-39bb-a1af-924bed5761fc | -7.6034 | -55.6995 | 2026-09-28 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| eb4d2a72-30e1-3c89-8e68-9a5c3a77d2fb | -10.6869 | -44.4576 | 2026-09-28 19:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 140b2074-b021-3115-a772-e10b498b23a2 | -11.1517 | -50.0603 | 2026-09-28 19:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 0ccac886-ccec-39f8-9c1e-4aed5997bdb2 | -7.4974 | -55.0256 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 0bc88cfb-181a-3b8c-b87c-7f0b6f9c24b4 | -9.0971 | -49.8836 | 2026-09-28 19:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| cf3f1a27-1de0-3d00-bd03-8f62f89123be | -11.5348 | -47.3901 | 2026-09-28 19:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| d4c7d18f-2c2e-3217-9f3f-7f2879009a41 | -7.7038 | -54.7521 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 0f22f60a-1660-3545-ba8e-ca6ade3e987d | -5.7384 | -45.0626 | 2026-09-28 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ff0464ab-e7cc-38cd-a1d7-5b735c2b574f | -11.4788 | -49.7646 | 2026-09-28 19:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cd0cf781-722b-3e4a-a4ca-223843a5d369 | -10.7916 | -48.7377 | 2026-09-28 19:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 52abdbf4-ab80-3369-a5e7-f922792c2014 | -9.9266 | -60.7171 | 2026-09-28 19:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 82db0775-d5b0-3759-9731-7f310af93e23 | 1.6749 | -55.9225 | 2026-09-28 19:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 011d38ae-d753-3623-8969-969b07c98c65 | -9.1682 | -45.7684 | 2026-09-28 19:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 04a30ed1-bf1c-3133-a92d-1d6beb9a31e7 | -9.9396 | -50.2304 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 321cc606-79d5-307f-8ab9-76a4ccca482e | -7.6851 | -54.7734 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 3a57922f-1e73-3c41-9931-655adb1dcbcf | -14.5171 | -52.4864 | 2026-09-28 19:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 7a7027d2-5258-3fcd-bfe5-5a30e060a57f | -11.5904 | -44.1411 | 2026-09-28 19:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 197b653c-8e4b-3d08-90d4-167360303cf9 | -13.9015 | -53.6548 | 2026-09-28 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 60331b2d-c0fe-3628-93ff-50e73f634852 | -10.9445 | -43.8849 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| f8b065ff-17c8-3589-8804-e74e3d25bf20 | -11.1327 | -50.0624 | 2026-09-28 19:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 39de6042-4a7b-3b72-8a4f-d67b31d79250 | -10.1098 | -50.1921 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| d8f1ce3f-d25d-30ad-8e1b-31640a21f311 | -11.9034 | -50.6175 | 2026-09-28 19:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 34ef6f97-f163-34d2-b7f3-a59d49c751a3 | -13.6866 | -56.6131 | 2026-09-28 19:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 237.2 |
| e6fc4b0d-abfd-3730-9e3b-9db979c59b26 | -11.8618 | -50.8572 | 2026-09-28 19:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| d19c8eb9-1176-3d0e-9e85-5d0c2a397869 | -10.9254 | -43.8876 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 28239e40-b65a-3000-95df-e2ab776d3e81 | -12.9457 | -51.0695 | 2026-09-28 19:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9985e3de-8213-36e3-98d0-61a29b688af2 | -8.2293 | -45.4375 | 2026-09-28 19:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5cb14eff-7b50-32b7-8c4a-e5e24cf48805 | -5.4949 | -45.1249 | 2026-09-28 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 190.1 |
| bc199fe4-2f3a-3ae3-9394-ab88ac66cc48 | -20.0991 | -57.2067 | 2026-09-28 19:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9e0a2f4f-d383-37c3-82eb-a70fe8d7fffb | -11.4601 | -49.7452 | 2026-09-28 19:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 713f49aa-906f-3415-a10e-9102e52ebe5e | -11.5384 | -47.1664 | 2026-09-28 19:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 3ca201a2-ab2c-3706-b0c3-b511625eada8 | -10.9637 | -43.8821 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 06dbaa18-e881-33d8-87de-67df409865d5 | -5.4762 | -45.1262 | 2026-09-28 19:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c76929dd-3695-371b-a569-496f4e39176e | -11.1775 | -44.7832 | 2026-09-28 19:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 264.8 |
| e0f2be32-2bc8-333f-806c-83d0067a0275 | -11.8641 | -47.1004 | 2026-09-28 19:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4a3644c0-6522-3064-823f-542c99892168 | -11.2753 | -43.5539 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 5c870a06-78a7-3596-8908-cd73de98fea8 | -10.2254 | -50.0093 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 917cf79c-96c4-3a7d-95fe-a8367c39daca | -12.0466 | -46.4897 | 2026-09-28 19:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 86a98e21-a3de-3d49-a093-d20747776430 | -9.9784 | -50.1412 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 3360bfe2-4351-3d8c-bc84-52271cf69b54 | -13.3073 | -43.9557 | 2026-09-28 19:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4719cb96-eeb8-32dc-a468-8ff3199e0794 | -12.5234 | -49.9834 | 2026-09-28 19:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d35dd786-4a57-3282-be93-068bba4cf4e6 | -13.4205 | -51.3304 | 2026-09-28 19:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7d0a1205-5111-33e0-89e0-c955f6f18452 | -7.6903 | -44.8761 | 2026-09-28 19:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3ecf30d6-cc5e-3090-a684-81503ff9c61a | -7.437 | -55.6291 | 2026-09-28 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 9f2440f4-03c2-3bec-9267-f8942796a8a7 | -11.0223 | -54.1379 | 2026-09-28 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| f5228e5f-5e34-35e6-8067-c06078aa87d2 | -11.6213 | -46.7742 | 2026-09-28 19:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| bc85b6c5-6399-33c3-b862-51bf172cf64b | -11.1962 | -44.8037 | 2026-09-28 19:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 6f12aa72-4270-33fc-8ec0-656f4079392a | -0.4889 | -49.1327 | 2026-09-28 19:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| b19652e3-46ce-3d1f-a4e5-9f5c2420f73a | -10.8185 | -61.3998 | 2026-09-28 19:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| bef65e17-d8a3-3fc4-92a6-39a50e3fdc97 | 1.8953 | -55.5841 | 2026-09-28 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 9eb26658-c243-3e33-9ed4-ab1ab17dbdb6 | -12.6071 | -51.9595 | 2026-09-28 19:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| cc3502c9-2d6c-3004-8ece-77b714fd83d1 | -12.9649 | -51.0671 | 2026-09-28 19:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 895.5 |
| b06d4155-9897-3d5f-9611-ed514d4255fc | -12.9646 | -51.0886 | 2026-09-28 19:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 3fbb4702-872b-3aef-8b46-9385822b98ef | -8.8043 | -54.539 | 2026-09-28 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 9d8b7fe0-7899-33ca-9a9f-683348429225 | -13.3262 | -43.976 | 2026-09-28 19:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 86476e6d-220d-3bde-9bb7-4e51e2fa0803 | -20.7755 | -51.3093 | 2026-09-28 19:00:00 | GOES-19 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 193.8 |
| 5c1431f5-cf65-3a38-99e1-06ff276949f8 | -12.0019 | -57.6051 | 2026-09-28 19:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 3a6e4d58-f46b-3fb3-b472-6867f6234da6 | -12.7677 | -54.0296 | 2026-09-28 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| f7be1904-9375-325d-8225-64870239fb3c | 1.8403 | -55.6046 | 2026-09-28 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| f7a0fd84-1717-36ed-be13-31c0a4ae4743 | -14.4151 | -52.8165 | 2026-09-28 19:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3149ee0b-63c5-3e79-a9ef-9407421eed7a | -10.824 | -60.7246 | 2026-09-28 19:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 207.0 |
| 9f253e17-44d1-3f1f-91bd-17426f1aabbc | 1.9501 | -55.7019 | 2026-09-28 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3c873f6f-fcb2-336d-906c-aee8c108c8a7 | -11.4791 | -49.743 | 2026-09-28 19:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3f9a68ad-44f3-3de7-bed3-e8e8f8067d2d | -9.0783 | -49.8853 | 2026-09-28 19:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| e539afea-6b64-3da0-b585-8ba5386a3299 | -10.2443 | -50.0074 | 2026-09-28 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 37c0942c-9725-33f1-a82c-878ef8fd3634 | -10.8052 | -60.7257 | 2026-09-28 19:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| a6470341-28aa-3607-a204-609bbc917279 | -15.081 | -54.5964 | 2026-09-28 19:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| c93d162f-caad-3886-b150-d2f800be60c9 | -12.0694 | -48.5377 | 2026-09-28 19:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3f987200-9783-3443-92af-28a4397840eb | -8.7264 | -44.9066 | 2026-09-28 19:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 6d273b71-09f2-37bf-8e9b-b54b662ece3a | -10.6505 | -50.7123 | 2026-09-28 19:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 0e9b61c1-4670-3a48-b39e-8288abf622ce | -11.0034 | -54.1396 | 2026-09-28 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| eb37da15-6937-3711-a87d-d143f581a787 | -9.6864 | -58.1258 | 2026-09-28 19:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 147.2 |
| b8931af5-540f-3569-8517-342e6b60dc98 | -11.5193 | -47.1689 | 2026-09-28 19:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 82d58017-111b-33d9-9104-8a8ae13d0f0b | -6.3137 | -43.6178 | 2026-09-28 19:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| da4b4e6f-447f-330c-868f-1c0fbfbb4bdc | -12.7868 | -54.0275 | 2026-09-28 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 8756dc20-a82c-3cd2-aa03-8f3dd9183e06 | -11.7178 | -43.4623 | 2026-09-28 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |


[Clique aqui para ver as próximas entradas](README178.md)
