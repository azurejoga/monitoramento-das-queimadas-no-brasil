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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb75777b-3c79-39d6-a463-9f8a2fb50460 | -0.82278 | -52.2718 | 2024-10-21 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80f677c1-de1c-374f-9a7e-d8f9df17faeb | -2.99677 | -53.0488 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6a31b678-93f8-3feb-a960-820280ce8764 | -2.99599 | -53.05369 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d87bedb1-c65e-3b17-bcc1-1d7582bb4b02 | -2.99371 | -53.04327 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4182877d-5aab-3e8d-9b22-3a7f419c2cdb | -2.99292 | -53.04814 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 426f04ab-c744-3b85-b2a5-6cdadad86469 | -2.99213 | -53.05301 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dacde06c-b277-3e94-abe9-a22a87ba3b42 | -2.98985 | -53.04263 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9b24d57-73b3-374d-92b7-9267b2e3c390 | -2.98907 | -53.04745 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3cfa3ff-bd43-329f-80d8-e651664445d8 | -2.97935 | -52.8488 | 2024-10-21 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c8b8c27-6e3c-378f-a48d-03566cc00f27 | -2.9786 | -52.85353 | 2024-10-21 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d4387ec-2dde-3689-9245-e8abffb3b78c | -2.97784 | -52.85081 | 2024-10-21 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e4ced47-a1c8-361e-b9bc-3e0ac695ee80 | -2.97479 | -52.85287 | 2024-10-21 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0db3e2-616d-3aee-8f0b-5049955f52cf | -2.95439 | -52.90742 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be9a246e-2129-3b3c-86cf-c6a52b22c651 | -2.95365 | -52.91208 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7dfbda-d083-363e-82b7-cf30daada718 | -2.95055 | -52.90684 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687390a3-304f-3e66-a91e-e65b14cb0c1a | -2.94981 | -52.91151 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3696d1d7-c51f-3589-acb9-9aabef4d3856 | -2.94672 | -52.90626 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d28bae93-28b9-33e3-a63d-2b85e21c4eba | -2.9175 | -52.4549 | 2024-10-21 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88134fa5-319d-3e01-b4e0-d3d5ca93df53 | -3.54337 | -53.02554 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fbe95f8-6d00-3fb2-8f1d-d1acb986c770 | -3.47191 | -52.21651 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f41d420-25c4-3e36-a6c9-e86f36cb135c | -3.47122 | -52.22078 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a248f9e-5903-376c-a2c6-06b735ed69d0 | -3.46757 | -52.22015 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45e3587c-5df6-35c7-bfa3-78454a4303dc | -3.46095 | -52.21469 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0f580e0-c084-3919-be45-fbc13d09489c | -3.40218 | -53.17733 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cca6d473-703c-3a8d-8b9f-000b26722f64 | -3.39831 | -53.17668 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 440ad0bd-2812-32f6-a221-7cd17b2d5c04 | -3.3095 | -53.37757 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90aa3628-df55-3434-8ba2-cc9e17962029 | -3.30558 | -53.37692 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63192ff1-bc22-305b-8f20-069cc04d093f | -3.4646 | -52.21529 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 782c8ac8-98d6-33c6-b38c-6ee2e9114c08 | -3.46026 | -52.21894 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 110d2888-7c25-399a-9d86-befbff8a4775 | -3.45729 | -52.2141 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc61921e-4f2e-3b53-a38e-0898183d0bd8 | -3.54415 | -53.02069 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c02fc3e-8c98-3ae4-9ba0-01b0884070b3 | -2.69035 | -52.06742 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c626d2-f1f2-3f2b-a525-57234499c4bf | -2.68965 | -52.07174 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc10d2ff-5221-3270-a176-0b8fed02397e | -2.68598 | -52.07117 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dee85d33-92f3-37d8-8217-b48cc55478ed | -2.85393 | -53.33689 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acac2322-b259-3546-8117-c8c12f513282 | -2.85161 | -53.3262 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eb97bc5-cdf8-3809-a547-8168c2f9f4fd | -2.8508 | -53.33123 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de33f10f-d617-386f-9ab6-ba37331cf370 | -2.84999 | -53.33626 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06d179f1-35cb-3b35-8071-e4c8dee086de | -2.84917 | -53.34132 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc0a6541-6369-3b49-a341-9df8ca4f4be2 | -2.84686 | -53.3306 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2f2ced6-2ab2-3645-a381-d4f5a0d593ab | -2.84605 | -53.33564 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50ab6791-b05d-3690-9776-b10bd44e2919 | -2.84523 | -53.3407 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f7cd1ef-a1be-3d06-82d4-65c656b6c958 | -2.84292 | -53.32998 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a5fddca-4db4-324d-9662-ca3ca66716ae | -2.8421 | -53.335 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bfd70a8-4666-3bf5-9c03-623ebcaddc93 | -2.84129 | -53.34006 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2a953bf-6543-34dd-bb29-dfc26356de43 | -2.83979 | -53.32431 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67443182-0b3e-3373-bf95-06fd8c061a32 | -2.83898 | -53.32935 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d7fe730-7e0e-3005-b4a0-88fed5a3e0b0 | -2.83816 | -53.33437 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0808e899-5f14-316f-9642-fc8e8b98070f | -2.83735 | -53.33942 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 249df6da-cf7e-3172-88cb-863f498764b9 | -2.823 | -53.00155 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b9115a0-9e79-324e-8f8f-206c2186387e | -2.82225 | -53.00624 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7b6e8cc4-852a-3a72-9f64-64b322eb6411 | -2.81914 | -53.00092 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e934e5b4-4497-3e28-96b5-4ab4002cf3f0 | -2.73787 | -53.20862 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a0e5c1e-4fc4-3b38-a26f-6d3ac05a462a | -2.73395 | -53.20802 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dcc3f1a-247e-3ebe-86a1-4872598eb465 | -3.45303 | -52.86436 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8933ec3f-75f3-3824-82e7-31fe8d995d57 | -3.37104 | -52.79669 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf7a084-51b6-3690-8d4a-a95faf1ad1f7 | -3.22216 | -53.37106 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8eae225-d1bc-325c-b53b-6e096631a0a6 | -3.11315 | -53.12384 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2253616f-1551-32f6-b96e-2579b30c7e77 | -3.11238 | -53.12861 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63977af5-083c-3be1-8482-775f808c8520 | -3.10927 | -53.12323 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 789da47f-7b70-3eb9-b79c-4055bc1ffa6e | -3.10617 | -53.11782 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b84d9a98-c4bb-387e-8afc-93a41534014d | -3.10539 | -53.12262 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 00451177-ad1b-39b5-99a9-e6422168b012 | -3.06615 | -53.24195 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25612a10-09f8-3cd1-a096-7bb578e0e16a | -3.06445 | -53.27716 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da5a2c20-3edf-3b44-b840-28fad7016927 | -3.06132 | -53.27167 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec26c81a-a931-32d7-b943-ad97acce5af2 | -3.05833 | -53.24075 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57689d2-38b1-355c-bbaa-44b8ce5be878 | -3.04972 | -53.24439 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1edbc394-5350-3af2-8e21-a02dc207a06e | -2.36136 | -52.5169 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae94d6d7-919e-3613-81dc-77e9379c324e | -2.36064 | -52.52145 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30ff53a0-87fb-34b6-991b-46c3ce3228c0 | -3.16761 | -53.06558 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c2bdd5b-06b2-3a42-a055-69f1e048bd76 | -3.12008 | -52.21367 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5715d46f-9755-31e9-9c6e-c75e6e75fa3a | -3.11702 | -53.12445 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9c8bcff-8e8f-3f7a-a0b2-36cfb066c337 | -3.11004 | -53.11844 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2c7e6352-4a62-30b7-8a41-5c3c3ae38da7 | -3.1085 | -53.12801 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a7e70aec-7364-33d4-bafd-e42325913e2b | -3.07006 | -53.24256 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 776a441a-0d9f-38cf-86a8-158d081b0f9f | -3.06694 | -53.2371 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e73b8397-1d05-3c76-9fd0-c7b362f9a6a4 | -3.06303 | -53.23651 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2fded6f0-ae40-32ab-9804-b8161bb149bb | -3.06224 | -53.24136 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 331c5692-917b-378d-bb00-fe8dbb38545a | -3.06145 | -53.24619 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17852a43-c0ea-3532-8541-ca75e6d79d56 | -3.06054 | -53.27653 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c1b5706-a614-3fcf-90bb-7fc693942b65 | -3.05974 | -53.28141 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7f1e90f-43af-3f4a-b7c7-b655c2e0f00c | -3.05442 | -53.24015 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76d03cbd-d31d-32d6-8c05-a4091218ec1b | -3.05051 | -53.23954 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75b6f12d-d4b9-3fc6-b5a0-8e698685104c | -3.0385 | -53.03549 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 045d821d-d5cb-315d-b7de-db203215f228 | -3.03774 | -53.04028 | 2024-10-21 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3075719-9913-342d-b345-b872dc068071 | -4.14707 | -53.88168 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 150f7a4c-ad7e-38fe-a82c-14238e0b6f29 | -4.06008 | -53.77635 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8960a61a-94f5-307f-b889-947fdabc0c20 | -3.79175 | -52.32372 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8747bdac-73e4-30f6-8648-5071fd1cddd2 | -3.79106 | -52.32798 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39caa7ab-4419-39d2-9b50-65c4d1d7dbd6 | -3.7711 | -53.40445 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51b85c34-ac90-3dde-8945-66681ec93a95 | -3.77096 | -53.40646 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 389a7e69-361e-33f4-8801-b337a9546db4 | -3.76798 | -53.3989 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86030779-39e2-35de-9411-7cc3c83bfdad | -3.76787 | -53.40091 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f8b73f3-6bc8-3300-896d-89f782caf5b0 | -3.7672 | -53.40382 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb1777de-7c65-3d06-a08f-fb95d208e9d9 | -3.74137 | -53.41494 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bf0f1f3-934e-3f80-98f7-01c497407662 | -3.56931 | -53.53355 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b29be394-4bca-3657-a321-4ff9fc648d5b | -3.56625 | -53.75432 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3e821c7-6a27-3d3d-9a77-f24bb49bc124 | -3.76706 | -53.40583 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fc3c030-e04b-3b66-b627-74d770106fe0 | -3.71897 | -52.28809 | 2024-10-21 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f2220e3-ee6e-34a7-bef0-1bca745d16ec | -3.56849 | -53.5386 | 2024-10-21 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README45.md)
