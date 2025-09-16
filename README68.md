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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd3f949-547a-323b-81c2-12c8d92bac4b | -12.67792 | -47.97989 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f25c30a0-7192-3b6e-9e0f-9706e3fde237 | -10.71204 | -46.49761 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7673a652-3032-3a22-b47c-6a789824f62d | -11.24209 | -49.94424 | 2025-09-16 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fcde513-3320-30a0-9350-3a1d01385fc4 | -14.82384 | -51.65996 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c5fc922-04ba-3370-8a5b-46793c12f442 | -11.44144 | -47.31004 | 2025-09-16 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c48ef845-9e32-30cf-ac84-9c69f8f2b315 | -9.09646 | -44.85374 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eacdbeb8-4e19-3f56-8fce-9bb52e8d6447 | -9.53846 | -46.30079 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5227d23-0902-3b82-944c-1dbeae29e9ca | -9.09871 | -46.93513 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a85346a1-d63f-38f1-b40e-22710d9671f6 | -10.78191 | -49.14051 | 2025-09-16 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b0321b9-d6c0-3b23-a4ed-980e5342fd51 | -11.27831 | -50.80175 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d4eef3b-2a8b-36b2-a261-1b81b2da4bf6 | -12.68859 | -47.99818 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19e85de9-061a-391a-bf87-38997edf2769 | -10.78045 | -45.97609 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0af2e8b3-0f5f-35dc-b2e9-9575d604b72c | -9.1372 | -46.95195 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05926185-9040-3496-af55-b86106dc8d0a | -14.8001 | -51.6732 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 94396834-c831-3ffb-9924-9a4e044d1de3 | -10.5631 | -51.94905 | 2025-09-16 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce932f21-376c-314b-9caf-00c2d93a67ce | -9.09965 | -44.86862 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ab292b61-6be4-3e05-acd7-f06fb3694730 | -11.70669 | -46.88386 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb43cc6d-25e9-3146-90b8-f8f94d06acfc | -12.96725 | -47.96456 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ceca277-7bb3-3ba6-a474-b32bdf68dcaa | -12.26163 | -53.91569 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de9451f9-bc9f-36b0-8211-7866a38d551f | -9.18088 | -58.8928 | 2025-09-16 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa7164f9-e244-3013-9351-3eff2c456cae | -9.98264 | -64.99917 | 2025-09-16 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f6c5c87-abf7-3735-b5c0-dc45fd9bc132 | -12.69451 | -47.9867 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35d6f531-b133-36c0-8ee9-18050a0cd4da | -12.80826 | -47.23423 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88944cae-4089-30b4-8520-6e8fa5aa5af8 | -12.83978 | -47.20537 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 91f51e8e-ebd5-387a-a387-240232182c26 | -11.11325 | -45.3322 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5a8e01f-7aa8-3db4-8cd4-e87bb5ae8e67 | -11.44182 | -46.9406 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd6b1981-5a50-3d85-9c9b-70a364845da5 | -12.29772 | -46.40551 | 2025-09-16 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58c6d001-e61b-305c-ac4e-0b087d17cfcb | -12.26383 | -53.92327 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae452cba-5880-3e8a-88a7-5074eadc9889 | -12.9818 | -47.95412 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b866facf-6d1d-36cc-b461-025c22d5f8ed | -12.66785 | -47.92348 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6b58826-edd4-3eff-963e-d0d19e980af6 | -12.76034 | -47.9701 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9f978935-911e-3f91-ac9d-8640ce85c707 | -12.11691 | -44.83113 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1942678b-403b-3875-8c6b-4406ccf3b927 | -8.98107 | -46.24382 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80b31145-e853-3b00-9609-df1c69475b55 | -8.61328 | -46.40102 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0311d457-35c2-32d9-8b71-cb2b167ecc27 | -8.65716 | -46.35138 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 282067b0-ba47-3a8b-853b-140203ef31f0 | -10.60284 | -55.39869 | 2025-09-16 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7b8a06c-1ab2-3222-859d-baecfb53b6b3 | -12.99961 | -47.95256 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88036054-245c-3cde-98ab-9ec8d6fc440a | -14.83917 | -51.67362 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89f65a8d-1303-39d0-b1a8-4ac43eb4d3b3 | -8.90436 | -46.15452 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c039bcd-b305-3e01-8300-1d597eab5674 | -8.67127 | -46.38161 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81aa4991-2987-3dfa-a4f1-a9c4169a1ab2 | -14.81282 | -48.12338 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c84c062-3118-31cf-8fc2-fe74a50f2e76 | -9.97699 | -48.36505 | 2025-09-16 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 166c585f-cae6-36df-bfdf-27b187ac1267 | -11.50176 | -43.72056 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3278a36d-d642-34e9-9440-2e8a93fae372 | -11.70808 | -46.86898 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef59538d-80a2-38f9-b407-d73dc033afdb | -12.29297 | -46.40484 | 2025-09-16 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dec96eb7-c6fc-3d4d-a6fe-e4459d225001 | -12.85776 | -47.14421 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1900dd10-a483-3847-a8b1-9dbcd9d74c84 | -10.47268 | -45.16408 | 2025-09-16 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92bc5897-d8a8-32ad-8ee2-047eeda8c5d9 | -10.36779 | -61.2567 | 2025-09-16 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25618749-718b-3fe6-9d72-3e57daaba8e7 | -14.9222 | -51.6525 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f71f7e9-aaad-3031-afa4-8895190aca85 | -9.09851 | -44.87729 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 76c4e225-7c00-3953-ab1f-c633c0f7d04b | -8.66807 | -46.37181 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0bb7996b-4eba-33ab-8a40-fb8fc4e8394e | -9.14767 | -46.94072 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f26848-c43f-31b1-97c7-c5381851f694 | -11.081 | -49.74868 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c21407fb-08fe-3779-b855-e8c8a38eccf2 | -13.02437 | -47.96494 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4cb7904-9357-32b1-b49a-296dcca7a585 | -10.41412 | -50.64513 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc5ffc5a-19ae-3631-b52b-dea6964e58ad | -14.03529 | -53.86271 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf26bdec-b670-3bbc-a744-97aa14704c21 | -12.61862 | -45.74646 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 027b59aa-1db3-3bed-9336-dfb7efeb89c8 | -9.0511 | -47.02045 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a096e2ce-fb3c-35ed-9123-5b3852e1b925 | -10.64509 | -46.22678 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb535ea9-6a03-3472-a73b-05e9696c0719 | -13.51446 | -44.30197 | 2025-09-16 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27be320a-8718-3026-9603-4b31cbe50de3 | -9.73264 | -48.12891 | 2025-09-16 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 172a9c47-7bda-3105-b60f-9939cc326f2d | -11.69334 | -46.87482 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 140df979-ad1c-3c57-b7da-5a766c3ba219 | -11.71208 | -46.87375 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1659f113-ec67-38e9-97c6-24a7993d1296 | -9.18439 | -62.52464 | 2025-09-16 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fc1f09b-ced1-3901-b8e2-1d5a01b187b9 | -13.20516 | -47.30646 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 14a053de-b412-331e-bb69-c6ed12567a64 | -12.10747 | -44.82063 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b5b595d-5da4-34ea-89c3-bc0f1931f29d | -11.43657 | -46.9454 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b5f07011-42f6-39c0-9d15-121da85609b6 | -12.11314 | -44.81814 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02619fe3-b3a7-31fc-94c8-8048fb0d8017 | -9.09889 | -44.87441 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 7efdc043-db09-38fb-87c9-81f3157476ed | -8.91499 | -45.52731 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20e4424b-d610-397b-b755-3d9d4dc1253d | -12.6179 | -45.75117 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99880cc9-ddad-34ea-9eb1-a3017a4466ad | -9.06731 | -47.03127 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2ac6cdba-2fd8-3542-8164-6e8937e5dc59 | -12.11652 | -44.83426 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 842595c9-18b6-3701-b218-d0fac000c9e7 | -14.20316 | -47.00958 | 2025-09-16 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 226372a3-1e30-3aab-8402-13dad99a60b1 | -9.18654 | -47.04482 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8420374d-ae11-37d7-bbad-a79551485a70 | -10.72888 | -44.75194 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b7fce41-dc2c-36af-b34f-5fa2d51899a0 | -9.0972 | -44.84809 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 134a5515-554c-3a3f-927b-8a26ad87babb | -12.84413 | -47.1383 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ece06b0d-2297-303c-92f2-33a682554249 | -8.58738 | -49.87233 | 2025-09-16 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef4df34-1d8d-375d-a563-895e744b3f6c | -10.72182 | -44.76583 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ede84502-bcf4-377a-a0bc-de262fba59da | -11.29668 | -50.85052 | 2025-09-16 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 107c8154-2998-3876-af8c-8250e4f5a17b | -14.3509 | -52.93024 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa251711-003a-3fac-9d7e-c84cf602f59e | -10.96 | -49.57235 | 2025-09-16 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 339a6505-ca19-3b3d-9aef-4eec0543d521 | -10.85276 | -56.36469 | 2025-09-16 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ed63f8b-dad2-3ce6-b717-bcd33075983f | -14.26895 | -46.14829 | 2025-09-16 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fedc0fc9-328c-3ed1-931c-8d2d37f2846f | -12.9742 | -47.9641 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8038b3c3-003a-3a5f-827c-43e8fafcf522 | -8.66743 | -46.37632 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36814419-8015-30ec-b6d0-2244f633e769 | -12.65059 | -47.95473 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dc07600-b186-3a79-841e-d97883927f47 | -11.11099 | -45.34958 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 390b332a-7814-393b-9f2e-ff984c9b711d | -10.40821 | -50.63603 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d883f5a-d2ae-3dac-9c10-1b422528cbed | -12.66979 | -48.00808 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 881af0f2-69ce-3532-8ca6-00311feee265 | -9.09649 | -44.86141 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ac7dc7d1-4368-3f2e-9b3b-904f7370135b | -11.72859 | -53.41832 | 2025-09-16 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a80f6f23-3a37-3a42-adf2-a6f0c04a9393 | -10.7095 | -46.51683 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| dab1c920-71f2-3670-80b0-2c1c5bbae9d3 | -11.11675 | -45.34464 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22318fee-abe8-367b-ba28-6573e6ddd231 | -9.09925 | -46.9313 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b3d780c-fc31-3917-8390-cc16ac22220d | -10.47732 | -45.16781 | 2025-09-16 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e09bbaa-b839-39b0-b53c-2f7f37251ba3 | -12.83798 | -47.21881 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3618f76b-8382-3c87-8726-fc6892f534fc | -10.6503 | -46.47217 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9864a3d9-6053-3aed-a72c-82812793df66 | -11.11787 | -45.33601 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)
