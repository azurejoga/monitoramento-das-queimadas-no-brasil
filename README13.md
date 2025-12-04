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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b4a2ff9-5ddc-3355-9e3e-ae557b6fb655 | -19.63614 | -56.8337 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d0930755-d6ec-3948-be19-36c91479d833 | -19.26939 | -50.56694 | 2025-12-04 04:23:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fa1de87d-de80-34cf-807f-373b47c563b9 | -19.61897 | -56.83966 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 307d6bf8-89c1-3f62-9be5-64c8b79a11b2 | -21.62957 | -56.13681 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e20a4c64-ff77-3878-877c-f21f6122a574 | -19.63175 | -56.8294 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 211b04d6-6e82-31f2-8b4e-d9a635c7c7eb | -19.63531 | -56.77032 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ade19dd9-6d0a-3b1e-806e-865a5905ce42 | -19.62335 | -56.84398 | 2025-12-04 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0bc5ddcb-a7e9-3696-bf00-b41256b3036c | -20.91786 | -56.36636 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f1581a92-0561-364b-b23e-f7a409aaaf59 | -12.62979 | -47.43097 | 2025-12-04 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbf8301e-718a-332c-a423-f254d6fb233e | -20.92154 | -56.37292 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d4de61e-4c05-3d94-a52f-e079c386918c | -12.63038 | -47.42733 | 2025-12-04 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93d4c562-7505-3b05-8685-11bb579a6c56 | -21.62128 | -56.12957 | 2025-12-04 04:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e105295-aa6b-38a6-8c31-bac9f05b4f3d | -20.92097 | -56.37029 | 2025-12-04 04:23:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27cfaf47-9cd1-339b-9021-d077cbf85ccb | -29.64225 | -51.70166 | 2025-12-04 04:25:00 | NOAA-21 | TABAÍ | RIO GRANDE DO SUL | Brasil | 4320859 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 56219432-fff1-3132-b1dd-497dcad82c98 | -27.82674 | -50.72387 | 2025-12-04 04:25:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd5b2278-d8f3-3d00-95cf-1638f07bbcf1 | -29.88555 | -51.21361 | 2025-12-04 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 0f517f8b-a8be-34f2-be78-f1b164820392 | -25.4481 | -49.16662 | 2025-12-04 04:25:00 | NOAA-21 | PINHAIS | PARANÁ | Brasil | 4119152 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8132f5be-4d12-3afa-9a2b-d4b799d144a1 | -27.82342 | -50.72319 | 2025-12-04 04:25:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25d07e7a-095e-3c16-969f-16abb9f13c27 | -27.68845 | -48.75229 | 2025-12-04 04:25:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 510db8b3-34da-3e11-a692-a5cee3d39fd3 | -23.6321 | -50.77433 | 2025-12-04 04:25:00 | NOAA-21 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f4d95406-ab1d-3740-8126-6de46cef744f | -30.8993 | -53.49838 | 2025-12-04 04:27:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 6110626a-9d90-3dfd-9a6c-fb50a1f7b379 | -19.6241 | -56.8339 | 2025-12-04 04:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 56607497-18d9-3258-b489-eaff42edce6b | 3.46897 | -51.25596 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a6c58fe-ec78-311c-8dc2-d2bc70b644af | 2.52154 | -50.85199 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f0d9c1-447a-3f88-bab3-641da7f10703 | 3.47535 | -51.25103 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1994c40a-d0d1-37d9-a4d4-c45d0608e32e | 2.53062 | -50.84306 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4f70224-a1b1-379b-be9e-0c9482b11d69 | 3.67137 | -51.2813 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3f2088d-0923-31c4-abc8-afa678b85016 | 3.47302 | -51.25219 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 523c5384-e865-3d77-976b-3f63f1d5b800 | 3.46669 | -51.26421 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83ca861c-fdd9-3110-8706-0c0452696e1f | 2.91706 | -51.01611 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ab1c97a-542b-3a26-b106-9d6d255e0fd1 | 3.47651 | -51.25164 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 713a1670-c418-38e5-a899-5a0d54b88152 | 3.58607 | -51.28651 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9a3866d-cb64-35a9-94b2-be6291031414 | 3.46836 | -51.25211 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60e5c289-5971-3797-94fb-08c88d8cf289 | 3.487 | -51.25002 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 219b5985-4883-31f4-9515-4daeaf136d92 | 3.67487 | -51.28076 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8e0055-efd4-33d7-b926-aa1f92464113 | 2.52721 | -50.84359 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cd574cd-a2a8-39a5-a2bb-f5b5488a5510 | 3.48001 | -51.2511 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89febbc6-08e5-3630-ad7c-aa4bd51cf976 | 3.4835 | -51.25056 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03b27efb-3def-3d09-a05b-8dc82dba6113 | 2.91304 | -51.01291 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c0387f2-1cd8-34dd-ab1a-a885e2bf7d42 | 3.46548 | -51.2565 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c184ba2-8467-3fb9-ac6b-3d4b281609e4 | 3.49109 | -51.25334 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dac2a922-f12e-3c4e-9b57-bef6e76f3984 | 3.67258 | -51.28906 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd691244-705f-356d-83ba-ef2aac4d4420 | 2.91362 | -51.01664 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84a7d70b-8116-3aca-abdd-28da8cebc911 | 3.48759 | -51.25388 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b48df76-56f6-3bef-b29b-8baf91692405 | 3.49168 | -51.2572 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88525e11-d1dc-3c34-912e-5a8a40de3bcd | 2.52553 | -50.85513 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 038fa970-0cbc-3bbc-8078-e5bf341a241c | 3.67899 | -51.2841 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03aa19e4-c4c9-3d54-b956-b163e928b814 | 2.53004 | -50.8394 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45d0098b-63a6-3b38-9fa4-bc4fd5cb8b58 | 2.9159 | -51.00863 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98497153-f7ca-3d8f-a897-c2599cf46905 | 3.58288 | -51.29067 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6f5ab02-4e80-311c-b5b7-506426a4a7e9 | 2.52779 | -50.84726 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 182bf70e-d92f-366b-b28e-788ec3fd2f10 | 3.58577 | -51.28625 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b39b13e3-57b4-3a7e-8821-3ab145521299 | 3.47186 | -51.25157 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 625d47f6-6dc1-35e9-85c5-20814a4e6d4f | 3.67198 | -51.28518 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8097620f-5f24-39d1-8057-28a4cc0b1a01 | 3.46608 | -51.26036 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8458499-8e54-3e16-a17c-86cc0a9ac0da | 2.91648 | -51.01237 | 2025-12-04 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be305093-f3a5-3f4e-8fbe-2415e6ca6aaf | 3.58227 | -51.28679 | 2025-12-04 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f80fbc6-ff66-309f-8589-a11629e9e122 | -4.20848 | -44.24726 | 2025-12-04 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| febe6131-a617-371d-9c42-c41cb94da990 | -2.64496 | -51.62482 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 683b16a7-36dd-3621-9887-61c667d17631 | -3.51592 | -47.20029 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcc20253-b69f-3dbd-9501-7911f24c71fe | -3.38043 | -49.2513 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5114564d-2ade-3e52-98c1-3a68c005c952 | -3.04866 | -48.42378 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6a8064af-7f87-38e1-b0f6-39d5f43b773d | -2.41478 | -49.34639 | 2025-12-04 04:48:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ae6e11d-e630-3a57-8aa6-4d7148764d91 | -4.73952 | -44.43559 | 2025-12-04 04:48:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60fed9d2-0267-3642-b874-377ba6d9e502 | -4.47513 | -44.25574 | 2025-12-04 04:48:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa19b024-72ee-3e9d-b4ed-33403fc9b648 | -4.40557 | -45.38605 | 2025-12-04 04:48:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614d7ca3-a40c-3add-bb21-48dc4a5c126d | -4.38835 | -46.6726 | 2025-12-04 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 772965ea-c9c5-35da-8365-891b23d9ed49 | 0.30941 | -49.81168 | 2025-12-04 04:48:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bde2f5a-5a72-3c4e-8fad-109d0fd9771d | -4.2175 | -46.45153 | 2025-12-04 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcb0d9f3-caec-30da-adf4-0b31a8cb574a | -2.5351 | -47.31843 | 2025-12-04 04:48:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dd6b7a3-d56b-395e-aeb6-a335ab2bc28e | -2.06723 | -45.35666 | 2025-12-04 04:48:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baea639f-2e97-3f6d-987e-baa0dafb3c28 | -3.93696 | -47.20234 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891489bc-e79c-3b07-aab4-0bcd38cb8165 | -4.50058 | -45.76896 | 2025-12-04 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 125b46ca-b269-3392-978d-7608eb11e1b3 | -2.60472 | -49.25423 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69e97ddb-e892-39aa-9287-8c82300b014c | -1.95663 | -47.90408 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e47ed4e9-23ff-3ced-b8bb-1b93fb417dd5 | -2.48381 | -47.83369 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8420f88f-83da-3e24-9465-80250b036cfd | -2.362 | -47.68624 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc6f06e7-8b40-307e-b49f-6496ea88ab9f | -3.93631 | -47.20658 | 2025-12-04 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cdd6a77-5546-34f3-af53-f6adbe6a39e3 | -2.60904 | -49.18285 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eae8aab9-dd7f-3065-9726-0b919923bced | -3.22011 | -48.62285 | 2025-12-04 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5ae2b2f-384f-3086-a83b-bfb858b3614b | -2.43764 | -50.2716 | 2025-12-04 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3324a62-c5ad-34ce-824b-41b16a6665ef | -2.38308 | -47.12951 | 2025-12-04 04:48:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ce2bfa-bee2-3335-b73f-5cc39faf90b7 | -2.92317 | -45.45532 | 2025-12-04 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bddcc84d-4339-3f9e-bc21-2d4c951a2d66 | -2.1439 | -47.88547 | 2025-12-04 04:48:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e86b2da-e26f-39d1-a2cf-a983b783dcc8 | -4.5649 | -43.8087 | 2025-12-04 04:48:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49585b3a-411a-34f8-a6d9-8a87d18a0dea | -2.04076 | -50.64045 | 2025-12-04 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf9b605a-20f9-3d34-abdd-a0dacf68f519 | -2.61141 | -49.25527 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55bc0f1c-c922-34cc-9816-f3fd46378267 | -3.77215 | -40.85025 | 2025-12-04 04:48:00 | NPP-375D | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34c8faf0-1d52-3266-9aaf-a35cd45e4d55 | -4.34768 | -46.14245 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd80d639-2308-301b-ac46-9499f2f7db7c | -4.34454 | -46.13693 | 2025-12-04 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff5ccb02-b0d0-33e9-ad69-005ace3332c5 | -3.14515 | -49.41365 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b34a6e27-ba48-3a11-8ade-4a467a4384ae | -1.67082 | -45.79304 | 2025-12-04 04:48:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8875ca75-2cc2-3423-8178-37c216cadda3 | -3.04523 | -48.42325 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51b2e8f1-fc7c-3e9a-ae4c-8b85d9efa45e | -3.32256 | -44.37992 | 2025-12-04 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b709202b-28e3-31e0-83cb-6ad6ca0e994f | -2.78683 | -51.67628 | 2025-12-04 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 597d6b30-1b36-3c90-a4c7-03297d2f5ce8 | -2.41384 | -48.08814 | 2025-12-04 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43caaecd-c71c-32fb-9af4-80e4b7b06f2c | -1.62846 | -45.42661 | 2025-12-04 04:48:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a03675e-b3a8-3393-9dd3-4acb23fcb6a4 | -3.05848 | -49.62212 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f06724c0-e641-32cc-ac1c-6fc42eddfd28 | -2.79023 | -47.43695 | 2025-12-04 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b5d9338-c178-3d84-bf9c-421c464e7312 | -3.13847 | -49.4126 | 2025-12-04 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README14.md)
