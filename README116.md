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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8106bcbb-b95e-32ab-a9ff-03366b433f3d | -11.1616 | -50.7008 | 2025-09-13 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 7d7cf5c4-3732-3ed5-bff7-bbdbf8813b17 | -14.1703 | -46.2505 | 2025-09-13 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 118.7 |
| ef52c8cf-2dec-3945-8599-39db455c9e56 | -11.0948 | -51.4289 | 2025-09-13 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0e8c5ef9-0110-3177-b3d9-7b73ec166b34 | -11.1619 | -50.6794 | 2025-09-13 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3b260aae-9cd9-3b7c-8405-1008106b1876 | -9.2472 | -59.4007 | 2025-09-13 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c4df5fab-5b1c-357b-a682-324297996d08 | -14.1893 | -46.2702 | 2025-09-13 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 6d0e645e-4c33-3ddd-b971-b360f81c41b8 | -9.2656 | -59.4191 | 2025-09-13 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 100d37dd-1217-3aaa-8fd1-a0c4c2a865d6 | -9.2844 | -59.3986 | 2025-09-13 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bf5c5682-7ae0-3735-b1bb-f984c893b4e5 | -11.095 | -51.4077 | 2025-09-13 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7eb85446-b5da-3681-9e64-74ec5f75dc93 | -9.5137 | -54.6292 | 2025-09-13 06:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 65fe05fe-a2f9-3021-8faf-cb06e6bad25f | -9.2843 | -59.418 | 2025-09-13 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 912fe1d2-2077-3bf2-8ced-b2c0afdb341f | -11.1426 | -50.7028 | 2025-09-13 06:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| ca53568d-14e7-3934-ae3f-de256bae27ee | -21.0839 | -48.9309 | 2025-09-13 06:30:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.6 |
| e30f1ccd-3e34-3ef4-aa26-fb74fa09cfb8 | -14.1898 | -46.2472 | 2025-09-13 06:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 976a5a68-b50c-3ced-be8a-618d01973607 | -21.0626 | -48.9588 | 2025-09-13 06:30:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| a74f8ade-df33-35ea-8ad8-e6e123ff43ac | -15.7815 | -52.25 | 2025-09-13 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| bc814c93-9bdf-35ab-991c-6a3ad018857e | -11.1806 | -50.6987 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 16686755-2040-3f39-8b22-5f5c894fab3c | -11.1619 | -50.6794 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0a629273-7199-3025-ac7f-ce1c88221913 | -14.2088 | -46.2669 | 2025-09-13 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b99f4b55-fa1c-3c0b-aca2-1ba1087a1ec6 | -12.006 | -47.7505 | 2025-09-13 06:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| eeb9c1c7-6768-3d70-b07f-3bd118cee6b1 | -10.8567 | -48.1827 | 2025-09-13 06:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8052cfb2-a40b-3f77-b9f9-6dd1114e1597 | -11.1616 | -50.7008 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 51dea915-6c7d-391c-85c5-50ec363c54e2 | -9.5324 | -54.6277 | 2025-09-13 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| ac7e62a1-7075-338a-9c31-393034e04c58 | -11.885 | -50.5768 | 2025-09-13 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 554a0694-3ef5-3fcb-97af-7376d0843899 | -11.0948 | -51.4289 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| f0c51f30-b93f-3590-933b-648a62cf0929 | -11.1613 | -50.7221 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ddb513b6-dea7-34ad-b9ca-032908ef0bd0 | -9.2658 | -59.3997 | 2025-09-13 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| a11e3ecd-dcf1-3598-9ac9-44532824e764 | -11.114 | -51.4057 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 74f79f9c-c411-3ea8-a2de-4ac7f7437054 | -14.1698 | -46.2735 | 2025-09-13 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 4fef1b86-ebf1-37ff-b0cf-468a3ffb97e6 | -11.1426 | -50.7028 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 167.2 |
| b52d41f2-b1d2-3bff-8e6d-c633b08eca9b | -11.095 | -51.4077 | 2025-09-13 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| bd3a79d8-8924-300c-9be5-7b4a98c798aa | -9.2843 | -59.418 | 2025-09-13 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 910bfe0b-b3a8-3964-a190-d6a064e640d6 | -14.1703 | -46.2505 | 2025-09-13 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5ec617dd-edaa-3bd9-b39b-7ba0c399e925 | -9.5137 | -54.6292 | 2025-09-13 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| d7680e47-c0e0-363e-9d3d-594c246a02ca | -14.1893 | -46.2702 | 2025-09-13 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 42004072-96bb-343d-a2ce-e357541b90b6 | -9.2844 | -59.3986 | 2025-09-13 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 880b36d5-35ed-32e5-93ad-5c374ad0191a | -14.1898 | -46.2472 | 2025-09-13 06:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 09d13be1-fd1b-35aa-b2ee-e3a1d25b51fb | -9.2472 | -59.4007 | 2025-09-13 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 0406e1a7-4731-314f-a4e0-025c4a67eb38 | -9.5006 | -55.9588 | 2025-09-13 06:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 072e8c03-df40-3ca6-9505-5a30bd48d6ec | -18.0303 | -50.9385 | 2025-09-13 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f5afe42c-a4cf-3241-b4fd-94d79d5b18e7 | -9.2656 | -59.4191 | 2025-09-13 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 3924db60-53ff-394f-9d4f-4e5f4dd3f0c1 | -6.56478 | -50.86377 | 2025-09-13 06:44:00 | AQUA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c55d5295-90dc-3d23-ab55-2e440ab2a55c | -3.43484 | -59.56688 | 2025-09-13 06:44:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9db2a694-800d-33a4-8ec7-d5b6d3472d67 | -3.44374 | -59.5682 | 2025-09-13 06:44:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6f12e447-f584-3f20-8118-e91ac823266a | 0.69219 | -50.63934 | 2025-09-13 06:44:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d864e90d-4ea4-33e4-a4ef-9690d5a781af | -6.56536 | -50.85853 | 2025-09-13 06:44:00 | AQUA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c1524766-0f22-323f-b6a8-e8cd5bba44ae | -11.13544 | -50.70044 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4081fc75-991a-30fb-9949-086ffef21313 | -11.10855 | -51.40309 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6c8dc2ec-1617-32f4-9cd8-4cf799a6809c | -9.50435 | -55.9555 | 2025-09-13 06:46:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 20fbc529-7d6f-36de-ad8a-5a0f9dede255 | -10.33404 | -54.31976 | 2025-09-13 06:46:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| c500fbc3-b121-3343-984b-6c0aebddbc65 | -9.27393 | -59.40502 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 821bf8d9-3013-3ff4-9aa5-cd92feaa9a43 | -10.40306 | -60.80507 | 2025-09-13 06:46:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1ea34aee-5b5e-3887-9776-8b31aafd2698 | -9.52792 | -54.62201 | 2025-09-13 06:46:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 70efec64-3936-385e-8f85-75819c38c333 | -9.52487 | -54.62711 | 2025-09-13 06:46:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 85a114f4-eabe-39ba-b8b7-836323760b32 | -11.14331 | -50.70578 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 530932ad-2cab-3810-b577-81157e206505 | -11.87527 | -50.57963 | 2025-09-13 06:46:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| dda03e35-8cb0-36a8-a9b6-b096f0a8232f | -9.25631 | -59.4024 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 6799610d-db08-3641-af94-7fab05a34a18 | -11.15175 | -50.70233 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 382.5 |
| 0b409258-c2af-3c1e-ac1e-3707791eb8d4 | -9.88421 | -58.3299 | 2025-09-13 06:46:00 | AQUA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31e27250-5d3e-30f2-8049-b869f5042f7a | -11.10386 | -51.41009 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 661af5ce-0616-3a95-bf0d-43538493ff77 | -11.08936 | -51.43206 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4410ffcc-515b-3d91-9373-861bb7caf3e5 | -9.50255 | -55.96834 | 2025-09-13 06:46:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 21aa1e95-c086-3cf2-8b48-031ea5b37dea | -9.49388 | -55.95411 | 2025-09-13 06:46:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e1c4f5fb-6670-3179-8354-f64b4b63ce13 | -11.1474 | -50.67054 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9c6afc1a-ca63-3af8-95f9-94909b09b197 | -9.52702 | -54.61051 | 2025-09-13 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1fe3c097-0c41-3bc8-9d78-fbcd601d6def | -12.91799 | -54.73783 | 2025-09-13 06:46:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 1f602f6e-a9a2-336e-bfba-84eb310333c4 | -12.92131 | -54.74545 | 2025-09-13 06:46:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 251ed372-5b51-30ca-9642-9db7ea38b6c6 | -9.51624 | -54.62083 | 2025-09-13 06:46:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 473b7ac8-af80-38da-8803-d47decbe24af | -9.27526 | -59.39612 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 894c4363-0a8d-38fa-a10a-57d3cf28e161 | -11.88152 | -50.58489 | 2025-09-13 06:46:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 416563ed-2ddf-3c28-af25-b410f21c87bf | -9.26645 | -59.39481 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8dab194d-a83c-3335-a846-fdeecff46968 | -10.09539 | -59.16168 | 2025-09-13 06:46:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b551cfec-0a8e-30e5-823e-5e157a5bb7f7 | -9.23278 | -51.23848 | 2025-09-13 06:46:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8b53a543-53ab-33dd-87cf-0b70b77776c1 | -9.4921 | -55.96693 | 2025-09-13 06:46:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 97a36058-6eae-3394-89f1-bf5df6299f03 | -11.07394 | -51.43021 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 9ce6cfcc-8244-3fef-958c-e157be4ced85 | -9.2346 | -51.23366 | 2025-09-13 06:46:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9464354b-dd24-390a-b5ac-6644a212daef | -9.51405 | -54.63687 | 2025-09-13 06:46:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| afd39c2f-56f8-33a0-a0e0-322855cfeee8 | -12.92358 | -54.7272 | 2025-09-13 06:46:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 05a96383-509d-3994-8e0f-1c0d1f657818 | -9.2726 | -59.41391 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f3f654f2-17f3-3d8d-8eb5-5375d6c4bb80 | -7.36112 | -59.95287 | 2025-09-13 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bd038fc9-38f8-3f59-bc28-77c20a56c86c | -9.26379 | -59.41259 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c8ffa57a-3567-37d7-a58f-1ac051ca23d6 | -12.90913 | -54.74382 | 2025-09-13 06:46:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6a57612f-f11b-3e39-a119-56790c5170e0 | -12.91562 | -54.75579 | 2025-09-13 06:46:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 21f9ba8a-90e2-3360-870e-d15dfdd9b4c7 | -9.80322 | -61.5128 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 87b41d2b-27bd-38a5-9317-36f9819b8b5b | -11.09309 | -51.40124 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 174.7 |
| f4399eeb-f193-3549-a72f-16df7ad0a9b4 | -11.15962 | -50.7077 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| e20c291f-0efe-3d74-afa7-90f91042e0f4 | -9.25498 | -59.41129 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1942e21b-e29a-3f97-9869-0ae447fbf51b | -11.1074 | -51.37918 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3d630724-89c4-3464-a9fa-ec096b278536 | -7.8595 | -61.1691 | 2025-09-13 06:46:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 99a6d525-56a6-37fe-a6ad-077efd349bee | -11.16375 | -50.67245 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 160.2 |
| f0bb3169-595b-3e38-82f4-88d980723b3a | -9.26512 | -59.40371 | 2025-09-13 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| d4928234-22e2-3890-b36f-0c69a7080eb0 | -11.07763 | -51.39939 | 2025-09-13 06:46:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| f0f650da-c858-3796-8c3a-07bdbc2f1782 | -10.00241 | -59.96908 | 2025-09-13 06:46:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 03c113c1-44ff-32cc-84fd-31ec9dad7d4b | -7.36359 | -59.81758 | 2025-09-13 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bd73abce-a3c5-351e-8b5d-0fa225ce709b | -15.77488 | -52.26367 | 2025-09-13 06:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 280af68d-2d34-32ba-b5f6-1082d0522f26 | -16.48904 | -55.13129 | 2025-09-13 06:48:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| fa608fe5-041c-3a7b-90fe-0555c2bbbfe7 | -15.77833 | -52.23326 | 2025-09-13 06:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 0e0e5cf8-e1e9-3021-bfe9-22a57903a17f | -18.03203 | -50.93258 | 2025-09-13 06:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e12ed80f-6815-3ff7-8830-85bc869bd318 | -15.7732 | -52.24057 | 2025-09-13 06:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1a3fb45a-1e2b-3e46-a0f6-4ec747d330bd | -18.03188 | -50.94071 | 2025-09-13 06:48:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |


[Clique aqui para ver as próximas entradas](README117.md)
