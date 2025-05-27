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
| 43ccb8af-2646-37b3-ae70-3de26ce66d96 | -11.56954 | -54.56063 | 2025-05-27 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e3afc6-fb8c-3851-ae6b-dd0232751481 | -12.0766 | -47.34932 | 2025-05-27 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8db37ce1-056a-3395-9ad6-2d5500e253f6 | -11.56679 | -47.44366 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb55c62a-b793-3a2b-b8e3-288511c08a5b | -11.13679 | -53.92908 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19d5ddb5-0d68-3227-a431-b3ff659460da | -10.82274 | -54.02542 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbe48729-4c5d-3439-9adf-46cf77f3124d | -11.14177 | -53.9191 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ef5cff6-9240-3e58-8b91-16a87e8dca9c | -16.625 | -52.13317 | 2025-05-27 04:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c53c8bf-a686-395e-8f50-5cd2cda47603 | -11.14397 | -53.92664 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b772787-734f-33e8-9200-034e158a6971 | -12.07601 | -47.3537 | 2025-05-27 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b40e5c91-93bd-3f11-b400-82a442d0ac55 | -11.82013 | -55.07228 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c027cfe3-88ed-3a00-96d5-c813eaa5a43c | -12.42331 | -49.97892 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e45e208-e9a2-3669-956b-6fb3d12675f7 | -10.73955 | -49.28546 | 2025-05-27 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87f47a0d-a96f-3fc6-b80d-c434e7b3168a | -12.52944 | -53.40678 | 2025-05-27 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e74455b-296c-3776-a0fb-372de18181b9 | -15.17262 | -52.29389 | 2025-05-27 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9453545-fcf4-3c1c-a260-d4e7bff5e7f4 | -14.01688 | -55.12663 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4704aec4-3af3-3bd0-bf0b-b6c348c70f79 | -10.836 | -54.02758 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de2c7429-6584-3f48-8903-7c483cee3e32 | -11.14122 | -53.9226 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fa3d631-2240-320e-9f89-60a6ee951596 | -11.4022 | -52.95151 | 2025-05-27 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eed4d21-7e95-34be-824b-7d2498058b17 | -10.81611 | -54.02434 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bede3045-5fbb-3182-aab3-2c49c65aa791 | -10.95696 | -54.37664 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c24cfad0-a8b4-34bb-bf2d-86cab4f17bda | -17.53489 | -52.12023 | 2025-05-27 04:51:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d8d323c-d6fa-3873-bcfc-ed2725c22936 | -17.53431 | -52.1244 | 2025-05-27 04:51:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57c049c5-e7a4-3ae4-872a-394920da606c | -11.79968 | -44.26995 | 2025-05-27 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 166509a2-d20b-3e35-b83c-7649e9f109e9 | -10.29409 | -57.13786 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6514d660-9bc2-393a-909e-987c22bc2f0f | -12.65738 | -52.44009 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0b9f42c-dd34-3cba-af3b-35cbc7dcd9a0 | -14.03178 | -55.13662 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e625110-ee8f-306a-82d2-480d1efa09a6 | -10.60079 | -52.84319 | 2025-05-27 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b0cc9d28-2a8b-3392-93ad-e1848731eb41 | -10.82973 | -56.96144 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5469d956-1235-37bb-a0a2-1588b151fe09 | -12.17065 | -54.26349 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10b705c4-c9da-343c-855c-d69dcf3602c8 | -12.27046 | -44.58567 | 2025-05-27 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ad1a6e0-f3a7-3d92-8621-ba4b77440644 | -10.82681 | -56.95654 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e50033fa-be7c-3bb1-863d-f6174894076b | -10.29705 | -57.14289 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f6a6be4-c012-300b-abaf-c15e12f66703 | -14.01849 | -55.13793 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16545d44-7ce6-35b6-bd7b-b9d78e40ae06 | -11.8067 | -44.26696 | 2025-05-27 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| def10838-9105-3a8e-a4e6-72b592c7e1df | -12.3679 | -49.98962 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd1bb01-b732-3d55-8613-6fc715d79030 | -10.84467 | -54.01451 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 806621ca-b165-3593-8ded-95805b436d61 | -11.13791 | -53.92207 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fb77e8e-3697-3cc8-94ef-a54f0dc451a3 | -12.37167 | -49.99017 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44a42018-5a15-3ce6-882e-835f1e0d4762 | -10.8188 | -56.95964 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0571732-2d9e-3f34-81d8-5ae28b8f34f9 | -10.82606 | -54.02596 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e214999-5582-39a6-b2ba-129a5c78a0c2 | -15.25215 | -47.4687 | 2025-05-27 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65862dec-6967-302c-aa5c-1dc05717f185 | -12.64508 | -54.07714 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ead8f47d-4095-332b-95bf-c00214412e19 | -13.0965 | -52.28925 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4ad97e7-ec0b-34fe-a126-e68ee1ac234e | -11.81955 | -55.07589 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95bc51f2-08bd-3987-99a5-db9832f52abf | -10.83324 | -54.02352 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45d4f1d6-3fc4-371f-8a0d-7b7155074fc3 | -14.03902 | -55.13417 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f8d9fe7-cbb3-316a-aac7-e33896813db4 | -11.39942 | -52.94743 | 2025-05-27 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06554e59-270d-3630-80c6-a90c5319f295 | -17.53132 | -52.11964 | 2025-05-27 04:51:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 822c6885-b6e3-3ff6-b62b-8625862e1937 | -12.35449 | -49.92122 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99c79028-d2b9-3f92-9215-47f5efd9feda | -11.13846 | -53.91856 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 340f70b3-7fef-3f8f-a3ea-4445035cd3c7 | -11.80014 | -44.2664 | 2025-05-27 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c508da0-cbf0-398b-959a-82bd0086dd44 | -10.29779 | -57.13846 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3000bd73-1f4b-33df-9424-24b98b2eeac6 | -12.35071 | -49.92065 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5511a552-63b1-3789-b7c6-aac9f77c6019 | -15.88523 | -43.43755 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8913ab-30be-3456-b3dd-f734433a6bad | -12.64839 | -54.07768 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0256dd8a-546f-31e4-91bc-85f344155f1d | -12.82635 | -47.40165 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2477dc6-662d-32ce-948f-78a650b698a4 | -11.77043 | -46.41433 | 2025-05-27 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f785eefd-00b5-30f6-8366-324c7058c1e3 | -11.6213 | -54.93547 | 2025-05-27 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 32318192-f9c1-35ea-8e04-e6cef6b68fe6 | -14.5935 | -48.35488 | 2025-05-27 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2e2cf46-176a-30db-a617-1d9a01232fe0 | -10.95306 | -54.37963 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 180e9e47-4cfc-3c6e-8d6a-700f34d43aaf | -12.64121 | -54.08012 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 138e1c34-d2ff-311a-8b70-5b213e82f020 | -13.78599 | -54.3149 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f3b7944-d9b5-31a7-b3a1-cc6e05124d85 | -10.8408 | -54.01749 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4af4662b-6c55-3d4b-9892-04289b81e274 | -11.55803 | -47.44241 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd1e8c4d-3afd-35cb-90a0-79b2973f39ad | -11.13735 | -53.92557 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23557e20-51f9-3f4d-9206-b59fff847e70 | -11.40498 | -52.95558 | 2025-05-27 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e30c15-eec3-3f03-84a3-bc25e853627a | -14.01746 | -55.12305 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c2f4703-9357-376a-aef7-9e39c84a0cad | -10.71714 | -49.62807 | 2025-05-27 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2abae356-c947-383e-9b09-1f75562b730b | -11.05363 | -48.8522 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6b101c0-fd5f-3c4a-b1a0-70c1b57c800a | -14.02514 | -55.13905 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1311205-bddc-37ed-9b7f-015f5409c88f | -12.41956 | -49.98109 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54b1113d-54c1-33fa-9141-c4260c106979 | -14.14499 | -45.46953 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63f6ab2b-c115-31b3-926a-8cca1683e4d2 | -11.8229 | -55.07645 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53e466a-3ccb-34ec-b160-4e02e52108c7 | -10.43423 | -54.64578 | 2025-05-27 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa63ef82-09af-3cb7-91ce-30b281217514 | -11.14066 | -53.92611 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82790d78-c2b3-3c49-9bd0-de9f49e446d7 | -10.83544 | -54.03109 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0ef306-5001-3585-8dee-bf412ab49dca | -10.73942 | -53.88628 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b6a18a-42dc-3b09-9d7e-77e7686889d5 | -10.30074 | -57.14355 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf4d30fa-b9fe-33f6-835d-4500669982f5 | -12.6585 | -52.43268 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b66560-c979-3578-88d0-de5c3a3df0a3 | -14.04017 | -55.12701 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c273ee9d-bc02-32c9-9a3d-8ee288f7cc7e | -16.99352 | -53.02753 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45d4a169-1923-3004-80a6-61ce345e0327 | -11.86888 | -52.2595 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11e26697-8324-37b3-b8a3-3990fa51d3ec | -16.56061 | -49.05754 | 2025-05-27 04:51:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad3350a9-f3ff-38ed-8d87-e1bef16617ed | -10.03069 | -54.32388 | 2025-05-27 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 600e66bc-51b4-3872-90ff-c4f38df36a88 | -10.95211 | -48.15673 | 2025-05-27 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65efaf62-cf8d-3a2b-8e1c-fd1624b9b0c0 | -16.99408 | -53.02365 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b5c5944-84c7-34e8-983b-8c8bd899aed9 | -10.84355 | -54.02154 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5dfe8c-d9d2-3293-9971-7bd0691f39b7 | -12.03574 | -51.59752 | 2025-05-27 04:51:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 611f3327-db7c-3bbb-b758-52d11a71b437 | -12.82874 | -47.38347 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd052c92-915f-3f57-ba85-be2bc806d67a | -12.41892 | -49.98571 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01fa36f9-ef7b-31c5-a8eb-3c8de7a02613 | -12.1141 | -54.66089 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3498f93-90ca-3fa9-b7ed-0b4fb03674b6 | -12.82695 | -47.39707 | 2025-05-27 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a068e8f3-4def-3569-b0bb-74d968ff215d | -12.03795 | -54.96394 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f57aa597-b7ab-39ff-a12e-467ad69b03a9 | -14.62637 | -47.94228 | 2025-05-27 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57bcb3f8-3969-3060-841d-7c5437ac9161 | -12.17121 | -54.25997 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a6e9aa-1b49-3dc8-9479-9fe859886b49 | -12.35515 | -49.91652 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 728333b4-01d9-302b-b9ad-6bf639d45fca | -14.01083 | -54.48238 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7e9f936c-68b4-3807-9e86-71034683f785 | -11.57118 | -47.44421 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5645cd24-de95-3a06-943b-5a203617937d | -12.42333 | -49.98165 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90e7b351-503e-31e9-9288-ee5c6b23d806 | -10.8239 | -56.95167 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
