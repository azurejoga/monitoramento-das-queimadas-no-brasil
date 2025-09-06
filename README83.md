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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 460df366-85af-3392-a354-5bd08ac13481 | -12.95475 | -54.7873 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92335ab5-aa7d-3d8e-8f66-4d5177e3dedb | -13.01669 | -54.84487 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ef10173-a0cc-3164-bb01-4a52a8199e8e | -12.35003 | -63.64365 | 2025-09-06 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3305a55-e8eb-3645-9c36-365104922af7 | -10.57936 | -61.2455 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 535c856e-6d54-30d6-bf36-a5e52b3c71b6 | -14.34114 | -60.32888 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d56f915-1579-3163-a9f2-5dc71bf3898d | -10.41859 | -60.74791 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff4dcccf-abe3-3744-bf80-c6d645703d13 | -10.57199 | -61.24796 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17e798d5-bfbd-3641-9c2c-b0268849073c | -15.71807 | -53.57018 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc48a8e1-3892-3435-a39f-6c59e56eb369 | -13.00108 | -54.84251 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55677e59-cfcc-3445-9a41-80333f5101c4 | -12.88583 | -56.94818 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c52d284b-297c-3c0c-b260-ebe1759ef633 | -13.00187 | -54.83613 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 131367b1-5879-3ac0-8dea-b9620409057a | -8.45183 | -45.03306 | 2025-09-06 05:31:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f4760215-e516-3650-ae68-33cbf5df9a05 | -13.00387 | -54.82001 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d649f869-32ed-3e01-aa5d-99bdd7526448 | -13.01309 | -54.83125 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3dc69f6b-512a-3412-845e-1e4a2880114a | -11.21415 | -55.02068 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77fbd06-40f0-3e52-935f-04e7703fc7c4 | -12.9621 | -54.81435 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70bba866-bc55-3bd0-9672-fe4bceece712 | -10.6097 | -44.31848 | 2025-09-06 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9b351c39-5889-3ef7-8539-12cdfa2b1a00 | -10.87909 | -55.73093 | 2025-09-06 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a400f6c-dab0-37de-9215-88753fd68792 | -13.00589 | -54.84645 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08cd433e-5db6-3947-bc00-b7b675ff955f | -15.20819 | -52.35798 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1becb0f9-1035-388e-9fcb-8fffd59622ab | -12.41769 | -63.90657 | 2025-09-06 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08e02c88-9dae-32bf-9a4d-468457f0197d | -14.17116 | -53.06727 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cec9d1ba-65a4-370d-a4ac-425bba58a675 | -13.00403 | -54.82555 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1e91d84-8cc3-3b50-90b4-f6ec6c900640 | -12.95321 | -54.80013 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d04bca3-a66d-3e9e-9564-d41f48c6d942 | -12.96326 | -54.80484 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8763a914-2bab-3958-bd3c-d1df489e7c07 | -13.00787 | -54.83052 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2b049b6-1a59-3989-8f83-159f7f643e14 | -13.00226 | -54.83296 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86d53bec-c6b5-35a8-9a56-801536d0eeae | -6.21615 | -43.57638 | 2025-09-06 05:31:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc280f21-c2ee-3de2-b517-8420ef137865 | -12.95634 | -54.7741 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d56cada9-3d76-3be8-9d7d-c51455e54673 | -15.13344 | -52.34219 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 407cffdb-1a9d-3deb-ada5-e283791ab065 | -9.99861 | -60.01418 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7be3d1a7-2272-3533-a8b7-46fd2a148a7b | -13.0179 | -54.83522 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 434aa7a8-84f4-3762-886f-a303bc4661cf | -11.20875 | -55.02291 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdaaf1e6-f5c7-3935-ab36-e6ee07dfb99b | -12.49813 | -53.86356 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 219f2188-e0ed-322e-b783-4ed9c80a2781 | -12.95842 | -54.80091 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cdafd92-6308-3bf3-bd1c-ddcf9af53637 | -15.72392 | -53.57109 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c11c487a-ea0a-39cc-92d6-38bcd7634c58 | -12.97217 | -54.81886 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d06f8314-40d1-336a-89e6-8571a0b79173 | -12.99905 | -54.81609 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b445a2e4-d6b5-367b-ad61-7eb4e43905c8 | -6.15713 | -43.17207 | 2025-09-06 05:31:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 74122a5f-d251-3e82-a985-2c44621255bb | -11.21918 | -55.02134 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1788e132-b588-3aa5-8b56-f3db7ee33841 | -12.99946 | -54.81282 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a6665ea-62de-3a04-8b26-bdc1a2d32d62 | -12.96287 | -54.80803 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4932560d-1313-3c73-b9d6-0a9f7e5ce277 | -15.58439 | -52.91776 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fe8e05ef-4bcc-3b83-ab33-6a1af3575cab | -12.49904 | -53.85619 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5cf9a3ed-7d9a-39b0-bd9b-5ded2eff78ec | -13.94084 | -53.99169 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1c43161-fc69-3638-a244-9f3786d446db | -10.25341 | -59.38758 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc44a0d5-06d5-37c6-94fb-ca19044973b0 | -12.96734 | -54.81498 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d068c01b-ee6d-3627-b79a-89bb0e7422b0 | -15.72247 | -53.5842 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 20153004-bece-3e68-b8a1-2f3c2ac1a254 | -12.61745 | -56.98852 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56e028f7-d09f-3d63-8962-417e0e24d4a9 | -12.95804 | -54.8041 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a196e336-f890-32b6-9f32-8d28824256b1 | -13.00628 | -54.84328 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0347c0aa-e441-3e2c-9699-05b1183336b8 | -13.0829 | -57.12385 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6412768b-5180-3620-ab94-4a18337f36bd | -6.3286 | -44.10166 | 2025-09-06 05:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5f0d90e1-531c-30ff-ad19-0aa4b4de8a0e | -12.09221 | -45.69382 | 2025-09-06 05:31:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 9dd7a8f5-137c-30e9-9b3f-2b3c2f132565 | -9.93764 | -60.10619 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc400f3-765b-3f54-8f4a-c3fe9bbaf7b8 | -13.00774 | -54.83918 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34420240-bcca-36ae-9206-b4cb934de7ec | -12.97139 | -54.82524 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c33e528-937f-3b73-b636-b0a7afa51943 | -12.42596 | -63.89709 | 2025-09-06 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88fa3fb8-ec38-32e0-b7bf-a5d1b7db79a0 | -15.84223 | -52.29179 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3cf61e89-1513-35db-8162-c2dc46cc9851 | -12.99101 | -54.79517 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de41a621-9d24-37b8-b4e6-d99ab20e95ca | -12.96365 | -54.80164 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a94b6908-1a47-35c0-9f54-5d3a7423aa15 | -12.96134 | -54.82065 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a4c49ec-6218-3ea1-91a4-77d686af84f8 | -15.8436 | -52.27855 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 828de669-9229-3949-8ee5-a9492f315a90 | -14.93945 | -55.89962 | 2025-09-06 05:31:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d8d2abc2-8025-3dbe-8799-3efea48e2a80 | -14.47192 | -56.8054 | 2025-09-06 05:31:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64bf0beb-9a5c-306a-8e23-242e6dfdaf99 | -15.69252 | -53.58653 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 65544176-6305-3ebf-b1a1-4320c138d0f6 | -9.69823 | -49.48428 | 2025-09-06 05:31:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 490cbf65-33e3-33b0-b69e-e06f3f4d4faf | -13.9288 | -53.99773 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e8ecfaf-24d9-3af3-9d80-d3a2bb208b2b | -13.00591 | -54.80364 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 326fddc3-2a33-3f82-85ff-42a0bc14eeb8 | -14.18085 | -53.06482 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93433a55-16a9-3103-95c2-59f7a3a8b820 | -10.16389 | -61.14135 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58d2e85d-1d14-3738-9f07-3785f68c9f72 | -15.85222 | -52.28273 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f8b35e3-eb0c-34fb-a5f4-4468241c06af | -13.01219 | -54.84636 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b88c293b-85f0-3188-8d46-e52e71fdbf97 | -12.98702 | -54.82755 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9446d54-3ea4-3428-91cd-a44d61700490 | -10.42207 | -60.74847 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56d4eb28-38ec-3bf0-bc5b-22f1774e8e14 | -12.99302 | -54.82193 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d57fd6c-ea1a-3849-8594-43488cb5102b | -13.00266 | -54.82978 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56b8f5f2-b48a-32f7-88bf-49573107f67b | -12.95359 | -54.79694 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fb4fc01-f620-3091-96fa-746c1e8a513e | -13.00708 | -54.83692 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c1dc403-de71-389c-84a5-4b244851571c | -11.21304 | -55.02939 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 610c0088-4e47-3e8e-9852-b431e29ff91b | -14.18037 | -53.06928 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e92cb2a1-bf60-3cec-9b85-17e4b43bf09e | -13.01749 | -54.83846 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f91b7a7a-906b-3014-b2c8-82795f8dbfc3 | -12.48266 | -53.85179 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 619727eb-0bd6-337a-a484-1da716021623 | -13.00365 | -54.82881 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4338ffd2-955b-35ed-adae-0b3c37fd308d | -13.01332 | -54.83675 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 610a7776-593c-3e97-9c78-54f425b7b83e | -12.95205 | -54.80972 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 872fd280-a219-3246-8042-481c0dd2f2d6 | -15.21036 | -52.37488 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0bd884a-5f24-3e80-af97-e512e1ff7304 | -9.71266 | -49.48664 | 2025-09-06 05:31:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 278910ea-1e18-34b0-b8e4-879aca38539b | -11.17998 | -55.04853 | 2025-09-06 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc1592f-c7c0-321f-bb00-1ebe53939f64 | -11.21268 | -55.03225 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 938ccaf8-d8f9-3670-b88d-31ae411abb6b | -13.00668 | -54.8401 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c310e447-ce5d-36bf-9cf9-eabacb68d5be | -15.84948 | -52.28398 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00c6f667-56e3-35b2-8ab9-7bc6c97070f4 | -16.63498 | -51.86367 | 2025-09-06 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8fa132f-697e-38a5-8791-07ddda09af2d | -13.01709 | -54.84167 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b919b794-ea64-376b-87a0-f1308b52b819 | -14.34185 | -60.32396 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f0d49b1-541e-39f6-acda-7bfeb6413fbf | -15.84266 | -52.28762 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d4d1c23-401c-3494-8e4c-fc3cd89b3dbf | -15.72211 | -53.58057 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d91ee844-3438-30b1-b3ed-7cb7d5fd1656 | -14.17166 | -53.06282 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 95240cdd-5e63-3328-b897-ae2f0c3f3b88 | -12.49261 | -53.86276 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07cc95e9-f34c-34ed-b3b8-6497fcd73297 | -11.32663 | -55.21766 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README84.md)
