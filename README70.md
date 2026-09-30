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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c866d795-3499-35e5-83bf-0c88939fc2d7 | -5.8714 | -51.7767 | 2026-09-30 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8c0e2216-2280-3192-a567-c90456669277 | -9.1525 | -49.9639 | 2026-09-30 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 54dbb4e6-d541-3860-b894-2bc85df86b40 | -7.3965 | -42.6498 | 2026-09-30 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| e4fb85d4-0701-3537-b735-e4b2ef75ffc3 | -9.8613 | -44.9577 | 2026-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 202.6 |
| ca909528-c851-3e33-b31d-c0b94f5d08da | -8.3802 | -45.4221 | 2026-09-30 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3beea686-026e-3a2c-b8a8-c3cc6e70b1fa | -6.7062 | -45.6216 | 2026-09-30 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6723d04c-bf9f-3363-ad6f-8a3c8a4ed150 | -12.6082 | -47.2429 | 2026-09-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 1ae72c0f-f32d-3334-8b12-37a5714ce371 | -12.6086 | -47.2204 | 2026-09-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| b8729914-e63a-3550-9e32-43f501405552 | -12.4351 | -44.1497 | 2026-09-30 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 4eaa34d8-5d4c-35ec-8cee-dd9d555e123f | -10.5496 | -49.7823 | 2026-09-30 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 02041aa2-847e-3497-8f41-8547e73db7fd | -13.3646 | -43.9929 | 2026-09-30 14:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| f47548e1-2ce1-35ee-ac69-06859a7c11cb | -9.88 | -44.9783 | 2026-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| bd400ac2-fe66-38dc-8600-fef9e03e44e4 | 1.6749 | -55.9225 | 2026-09-30 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e53944e1-d2d8-3115-ab0c-ccf20ee5b248 | 3.64 | -60.5086 | 2026-09-30 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b0135940-5ee3-3bc5-b00b-f53c0279b259 | -7.2944 | -43.3191 | 2026-09-30 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 61c732aa-5dc6-3b0e-8901-a61236bfadc6 | -9.4328 | -50.1086 | 2026-09-30 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 60ea02aa-3191-320c-a6c3-4d14e8d39cb1 | 1.7115 | -55.9221 | 2026-09-30 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9888b2ad-6f84-3e67-ac75-072423a5d0bc | -12.6275 | -47.2401 | 2026-09-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9c71758b-63bd-3b0d-b523-1b4b415de07c | -12.7618 | -47.2431 | 2026-09-30 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 12ec184f-40ba-316d-93ac-b690e8ee2752 | -17.5137 | -43.7183 | 2026-09-30 14:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 8b101625-cded-339a-81e6-0467902d0617 | -10.907 | -43.8433 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 9d0f5f7a-2a08-346f-b8d5-f033a71f121b | -9.8064 | -44.8265 | 2026-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8e589fa5-2b68-3e9b-8c44-cee7f76c9d40 | -16.1671 | -42.8587 | 2026-09-30 14:10:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 439.1 |
| cdb8bc4e-d68f-33f8-bcc3-8208d8c1a019 | -14.3348 | -44.9017 | 2026-09-30 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 73294716-4962-33ec-bbfb-866a802b4933 | -11.3743 | -43.3734 | 2026-09-30 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 1c0d69dc-c80a-3131-a8e4-fd5e0ee79d51 | -17.5338 | -43.7135 | 2026-09-30 14:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 256.5 |
| be7fa624-ae8a-3ce9-8a12-fd95eb4f6e0b | 1.675 | -55.9028 | 2026-09-30 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 58cdf29a-b47c-3ef4-af2c-faf3db3cff0c | -8.0355 | -42.866 | 2026-09-30 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| 9ef3940d-7357-3ba0-bf32-d802a053f5b9 | -12.0694 | -48.5377 | 2026-09-30 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b9d5a14f-85eb-371b-a8a8-ea87e527eed4 | -9.7687 | -44.8082 | 2026-09-30 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f4caac54-db80-331b-ae00-93c75e48d537 | -11.6797 | -44.5012 | 2026-09-30 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 3731d48b-41ec-3bf8-9948-8d6e3fb52794 | -5.73 | -45.14 | 2026-09-30 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d3ee88a-b822-3724-90bb-8c43fe6a5158 | -5.76 | -45.14 | 2026-09-30 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09b06f49-357d-3acd-8173-9d373e4b3a7d | -5.76 | -45.19 | 2026-09-30 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b9674c2-3e58-3bcc-af09-e15d9dad3900 | -6.7254 | -45.5749 | 2026-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| de215ad0-cdf3-35bd-8f3c-85df88033653 | -9.9956 | -50.2675 | 2026-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 70910392-c5f5-3701-b440-dbcd5b1c99e3 | -10.2843 | -44.6274 | 2026-09-30 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b6df9a3b-ee06-3eec-a8eb-12482f4394be | -8.0166 | -42.8681 | 2026-09-30 14:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 174f58b5-b594-3a73-9509-fdb5173923a1 | -9.0463 | -45.0083 | 2026-09-30 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| e8b0b217-abf3-3002-b498-8fe403d8e8a5 | 4.1884 | -60.63 | 2026-09-30 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d7dc24c6-3f9b-3e8f-a52d-fad1cc268ccd | -10.5496 | -49.7823 | 2026-09-30 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 23887926-77cf-355e-9557-dd16683a6c46 | -7.0547 | -42.8726 | 2026-09-30 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 73bba979-e661-3b5e-a8a9-28332ca1e36c | -11.1767 | -44.8296 | 2026-09-30 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 1c307843-56ed-393f-80bd-9aeddefb382e | -11.3743 | -43.3734 | 2026-09-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 028159db-e0f0-3dc8-b0e6-019d54a659a3 | 4.2067 | -60.6296 | 2026-09-30 14:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7358175c-42a2-3408-8cc7-bc98bb7cfffd | -8.2102 | -45.4621 | 2026-09-30 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a2828dc3-bf7a-3e4c-8563-9553570bf0b0 | -12.6082 | -47.2429 | 2026-09-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 6cd16417-9031-3658-8482-681950f1b963 | -9.9396 | -50.2304 | 2026-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| cad05658-41d5-3317-8d1c-3a3d6c98e6bf | -16.1671 | -42.8587 | 2026-09-30 14:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 202.4 |
| cf7d4f69-6dc7-3e65-9189-a663e90bf4e6 | -11.2095 | -45.1478 | 2026-09-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| d857f49f-c5fe-3cab-b7fb-01fd8e21c2a6 | -7.4156 | -42.6241 | 2026-09-30 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 45d49320-7c2e-3c5e-8dc1-25dfee4e9922 | -6.1598 | -52.9134 | 2026-09-30 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c79c1415-17fa-37d2-8fb9-a2734098b27d | -11.1942 | -46.0637 | 2026-09-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 058265a6-ad76-3178-bd18-67dcf5759a09 | -9.0652 | -45.0062 | 2026-09-30 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 1a33bbb5-2cb2-36a0-9cc1-0aa736487da2 | -6.8762 | -43.7083 | 2026-09-30 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ab920165-9e56-3d89-869f-18a970d904f0 | -13.3646 | -43.9929 | 2026-09-30 14:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| ab85fefa-183b-3a27-a724-c275d784336f | -11.1958 | -44.8269 | 2026-09-30 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 19fd9cde-f718-3127-9215-ae32f1a3c7f3 | -13.5344 | -49.1731 | 2026-09-30 14:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 48012027-796e-3d00-8cbd-9ea6c7b63a38 | -8.0355 | -42.866 | 2026-09-30 14:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 2915d433-5add-3697-b884-15d79366a1a5 | 3.5313 | -60.1494 | 2026-09-30 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 43ec6c4c-acab-3aa2-baf5-a99941446b0c | -7.3656 | -42.0819 | 2026-09-30 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| cf45d3c5-bcab-3929-a353-ead40cf60293 | -11.1954 | -44.85 | 2026-09-30 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3ce932d8-1d7a-3059-a5f9-1ec9a18b0da7 | -13.3658 | -46.8366 | 2026-09-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 1d9892f3-bfdc-372f-a75d-99a277f8d782 | -7.0612 | -42.3035 | 2026-09-30 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| fc416017-8619-3875-a446-a1ad8ee13bb7 | -7.506 | -44.5503 | 2026-09-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 816c2f46-19bb-3dd0-8045-227603e246ee | -9.1337 | -49.9656 | 2026-09-30 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 55ddce79-0f96-36d9-a968-473449d7ec8c | -9.4813 | -46.3646 | 2026-09-30 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 654dd5ee-371b-3c44-b845-f7b5e1e991ee | -8.0169 | -42.8444 | 2026-09-30 14:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| c41404a0-0afa-3d69-8f2e-9ffe8cb7fe66 | -12.6275 | -47.2401 | 2026-09-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 45db639e-9b0b-3455-894e-38464138c712 | -8.3397 | -44.1658 | 2026-09-30 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 3cec59db-d636-302a-9471-c2b2aab55898 | -6.7062 | -45.6216 | 2026-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 50f1a2a7-5519-3300-a3c3-dd193b679c42 | -6.914 | -43.6816 | 2026-09-30 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| acde8cb1-29a4-3b30-bbee-a7fd88be3810 | -6.8764 | -43.685 | 2026-09-30 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| efdac8c3-7bbe-35ae-b212-123e2cdcdd1f | -12.4351 | -44.1497 | 2026-09-30 14:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 369.8 |
| 3d7be6b1-832a-3051-80c0-5c03db6ddffd | -13.3469 | -46.8169 | 2026-09-30 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 31082a68-6272-3f12-9820-ad65676cfed7 | -10.2827 | -49.9606 | 2026-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3ef5abf3-1ed6-35f2-867f-8a698ce6d8c4 | -9.4328 | -50.1086 | 2026-09-30 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 79e44cd3-c2b9-3b4d-b7f9-1394571210ec | -9.0466 | -44.9854 | 2026-09-30 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| dc069c3a-ab84-31e2-8b4b-8725e4ed44a2 | -7.2564 | -43.3462 | 2026-09-30 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| aeaf5de8-03a2-318d-b077-2527f3d4230c | -11.6592 | -43.5188 | 2026-09-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 1aaab6ae-7206-3e8d-944b-ccceda2b4fe8 | -13.3835 | -44.0132 | 2026-09-30 14:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| f0a6af86-09f5-357b-a5c5-6a3caaa4d93d | -11.6395 | -43.5455 | 2026-09-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 29832f80-7e55-382f-8e2e-c8a9c9ed7445 | -7.7086 | -44.92 | 2026-09-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 718dbe26-b6b7-3149-a9cb-8359a6f3ce25 | -5.8714 | -51.7767 | 2026-09-30 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4886a57c-142c-3650-82d9-a4f8c0db1184 | -9.8617 | -44.9347 | 2026-09-30 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 3254f980-960c-3d24-bff6-103ce66ef45e | -7.3967 | -42.6261 | 2026-09-30 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 52e05147-7698-37ee-a3dc-6279bede3511 | -11.2566 | -43.5331 | 2026-09-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| b9bce9da-a078-3cfc-af0f-fbda5e3adf19 | -8.9147 | -44.9544 | 2026-09-30 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 24428d47-627a-3f56-8445-4c83aac05178 | -15.2733 | -44.8192 | 2026-09-30 14:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 3d46c981-b639-369b-bfc0-cefb80119b9b | -10.0145 | -50.2657 | 2026-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 88487d4b-9e8b-337b-8f81-5c2a42e5fd58 | -7.2752 | -43.3444 | 2026-09-30 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 56c22b33-eea6-3065-b390-fd0544e072ad | -7.2561 | -43.3697 | 2026-09-30 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 78d63790-cf9d-38f3-99ea-49625f6ae39b | -11.1903 | -45.1505 | 2026-09-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 24880352-9118-3aea-9631-cb7df0703420 | -7.3653 | -42.1058 | 2026-09-30 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| e756f9d2-260e-3d3d-9374-29d88d08fb66 | -6.8195 | -43.7366 | 2026-09-30 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 3bc298de-4e02-33b1-999a-7fe42b2ee6e4 | 3.5312 | -60.1684 | 2026-09-30 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6c911799-de01-34ff-b77f-dd95a41a5abb | -8.915 | -44.9315 | 2026-09-30 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| c8ff4b7a-406b-3dee-8444-149ce6a8b506 | -8.3802 | -45.4221 | 2026-09-30 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e379c1c8-af15-3e1e-9f41-713b4fb7210f | -11.64 | -43.5218 | 2026-09-30 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 4341bf17-0074-3d7d-b671-eaaf60917e99 | -7.3965 | -42.6498 | 2026-09-30 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |


[Clique aqui para ver as próximas entradas](README71.md)
