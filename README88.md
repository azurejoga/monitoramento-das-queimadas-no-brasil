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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b452b933-826e-3423-b7ee-0659ea3e2fb4 | -9.11946 | -60.40104 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a95ce81-52ed-3c3f-8ef5-3fe2839c022d | -9.02706 | -60.43749 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48dda95b-aecd-34a1-b638-495ab352cec4 | -9.02417 | -60.42889 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0100d1fa-8ace-3eb7-91aa-005faba6a87c | -9.0235 | -60.43281 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03334cf4-21a7-3792-9b8a-6e03fab1b18e | -9.01995 | -60.42812 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30f02133-1dca-3c39-b5b1-844cfd3ddcd9 | -9.00793 | -60.42203 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45dcc04-eb3d-36c0-8a9d-b02bec2eb17d | -10.42296 | -60.98882 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8873c624-6410-34a7-9a75-00e5e888a7ec | -10.42226 | -60.99281 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 005cc280-f59a-37f3-b499-ad1a933aeeea | -10.37698 | -61.17294 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd822350-899d-3748-a82b-5bca645bc6a7 | -10.37624 | -61.17712 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ee700c-1b81-39fd-8118-737e05382035 | -10.067 | -61.11519 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7fcc2a2-72aa-3eeb-8b54-ffa500066400 | -9.95701 | -59.84273 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3efe2cc7-2a36-3bc8-9bc5-91f7cfd8c4d3 | -9.95641 | -59.84623 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d1fcb92-06cc-379b-bbd3-e8e540a02067 | -9.95179 | -59.84902 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47dd44c1-ca11-3aef-95b8-abf32fe68b6f | -9.95134 | -60.14201 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c326395-fe18-363d-be75-c6692e967c59 | -9.94788 | -60.13761 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca65ffb1-8ff2-3f74-b787-2f3bced75f68 | -9.94724 | -60.1413 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e34273c2-0216-37d2-95fd-75b227b3d242 | -9.92359 | -59.93934 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90376799-a458-3517-b1c6-09261cf257e9 | -9.91226 | -60.17282 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9defba7c-68dd-3fc1-9c17-f76feb246e8e | -9.90816 | -60.17213 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea96e086-14e6-34a5-a098-371b4b6a895e | -9.90752 | -60.17581 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df3564c-311b-3cd2-96d7-95ceafafa9de | -9.90405 | -60.17143 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c5765f9-9366-30cd-a755-e9626b5d2a22 | -9.89412 | -60.42528 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35f71b1-d3a2-372c-8559-7fb89d8433b0 | -9.88483 | -60.30607 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7004de5-eccf-3d17-9427-9c5fea366120 | -9.88069 | -60.30537 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1f39ae2-a42c-365b-b190-4cfa393b219f | -9.88003 | -60.30914 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63200703-1d78-3310-a272-17a40d7d9412 | -9.8759 | -60.3084 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e02b4a-699c-39a8-944f-bf48bcc5f2e9 | -9.87589 | -60.79814 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de91e817-a97e-38ae-89f9-85f759e499fd | -9.87516 | -60.80222 | 2024-10-08 04:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b45cb9d-d958-350c-8c19-e5739df46c29 | -9.87385 | -60.1509 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16bc296a-a1ae-326b-b4f9-e0dff1506cee | -9.87243 | -60.30385 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7fb109a-a1ab-369b-91bd-56edf779710a | -9.87176 | -60.30765 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ee791c1-7c7b-3410-9e5c-7b18e9427852 | -9.87109 | -60.31145 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b95b8b2d-a276-3594-8147-bb7a9e4cc4ae | -9.87096 | -60.15083 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 861400ad-723f-3f5d-8f6a-f63054c89bc2 | -9.86975 | -60.1502 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 651d3cf6-e8b3-3d16-8209-9969052192b9 | -9.86686 | -60.15012 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6391692e-8a96-3059-8004-da88f3dae3ca | -9.84414 | -60.29494 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aacc5a4f-a462-3fea-9104-2331d31ad272 | -9.84347 | -60.29871 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deb0a7d9-1411-3447-8911-98f8ba03b493 | -9.81435 | -60.46275 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1beba08-470c-3207-b9fb-eff2a621bb94 | -9.81365 | -60.46342 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 002792f2-32aa-31f8-8db6-5be8265177c0 | -9.81212 | -60.44708 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29ee7b06-0c5b-39aa-96f3-9b219543119d | -9.81017 | -60.46196 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43e00842-e07e-3900-a1f9-4f9e71b86836 | -9.80948 | -60.46583 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf593a32-1b67-381a-a7b8-1f6fd260e243 | -9.80947 | -60.46263 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac35ec66-b254-30d3-90b1-f33f3e6258d3 | -9.80926 | -60.43863 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd3e3035-8f4c-3a4f-b3b6-655ff7cf5c8f | -9.80881 | -60.4665 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b2beaaa-5f6a-37a9-8181-49382e0b64c3 | -9.8086 | -60.44249 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a54870a7-31da-38b9-a112-ebc42a12ddcc | -9.80794 | -60.44635 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d22651-30cf-31a9-b629-c6b41fd7fc92 | -9.77617 | -60.48061 | 2024-10-08 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696cce5c-688c-3b08-947c-5335a3315027 | -11.43299 | -60.45543 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 141f6767-e471-3289-bb3e-f94ebee4f28e | -11.39052 | -60.40993 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d397210-2828-3831-9547-8bbf860035de | -11.35793 | -60.57149 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30b1263c-bcf6-3250-af03-3a7a3979820a | -11.35384 | -60.57059 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e1d939-be18-3103-b70f-4078d9dca568 | -11.32905 | -60.54313 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8231551-0c75-3ecf-9944-a7b6b06c8286 | -11.32495 | -60.54239 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59ff6e10-6147-3594-a3ee-5e0c2ee2bfce | -11.28469 | -60.32318 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a6f7a02-8b61-396a-b569-16dcd8c59604 | -11.27895 | -60.57267 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6c6d9c7-4c54-36b5-9bd7-07af14edb442 | -11.27763 | -60.58025 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 019a99e8-1783-3007-bbbd-84cb3be326a0 | -11.27699 | -60.58395 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 272f4917-2de0-3f04-80c6-094927105f5c | -11.27486 | -60.57179 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ee5c0fc-2e99-3090-9dfa-e827120118e5 | -11.27356 | -60.57924 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| effe1a33-16da-3720-a006-68a49f1b7265 | -11.26574 | -60.38321 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f38ba43-bb00-307b-9b99-f2f762f64df1 | -11.2651 | -60.38686 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f83dfd9-5f25-3c33-8df0-754036e04927 | -11.26443 | -60.39063 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5c29c9b9-9840-341f-9b16-3e58b1a7a5ff | -11.26316 | -60.56585 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a062e4e1-aa66-353e-9aaa-d017aa4be079 | -11.2617 | -60.38235 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c013e3e2-13c9-3ca6-aaa9-b1e623c0195d | -11.26105 | -60.48146 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ed18620-8c12-3562-ad38-bf78a0915b74 | -11.26043 | -60.48495 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4772a8e8-f45c-3c0c-bccb-0fbddd01c058 | -11.26035 | -60.38997 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8bf0056-8bb0-3e0e-bd8a-aadb0332128a | -11.25981 | -60.48849 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc3432a3-d0de-38bf-8308-2e562afc16de | -11.25966 | -60.39391 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e508cde8-56d4-3183-b80a-5ee36d7d1da1 | -11.25761 | -60.38177 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed4b534c-1597-3e01-b267-37196d2f75bc | -11.25698 | -60.48058 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2766d52-e67e-3ea8-ae42-cfcf0a8d3588 | -11.25574 | -60.48764 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 416285fd-bcfd-315f-99e6-42fae975e75a | -11.25556 | -60.39336 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2804dd1-528e-364b-b226-d8e552c31887 | -11.25485 | -60.37365 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f7fd984-8918-34d3-b781-0608056ae089 | -11.25446 | -60.49486 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfedd9a7-706c-39b8-958b-e408526e6860 | -11.2542 | -60.37736 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e25d497e-0d29-3782-8a5a-7286c3d06f98 | -11.25361 | -60.57189 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7641bbdc-182f-32aa-a5e8-4deb944b199b | -11.25145 | -60.39283 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecbbccbd-221e-39fd-8600-6bc72025fbd6 | -11.24973 | -60.49771 | 2024-10-08 04:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc2d1fea-bb43-34d3-9b44-c0c0735fb56c | -11.24944 | -60.57148 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0144001b-9763-304c-9669-bb5ef9cdad19 | -11.24084 | -61.18253 | 2024-10-08 04:57:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80f849b7-32b3-353f-b049-bb8908b08f23 | -11.24011 | -61.18662 | 2024-10-08 04:57:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d223af16-c7ca-3928-a52c-dcb53a293d65 | -11.23583 | -61.18576 | 2024-10-08 04:57:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21f02f4e-01b4-3134-aaab-356e30830957 | -11.23303 | -60.59217 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40cd9a5a-56a6-3a62-8f5f-483132348de4 | -11.23293 | -60.56876 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 672caa93-bddb-36f2-9a27-c76fef300b5e | -11.23237 | -60.59593 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f30d1e4-8ada-347d-b0ad-682390cbda89 | -11.22949 | -61.17183 | 2024-10-08 04:57:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7de81b0a-6fdf-3327-b923-939da920cb45 | -11.22815 | -60.57173 | 2024-10-08 04:57:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5c2a69e-1afe-387f-a221-5c756bb83d46 | -13.3958 | -61.93529 | 2024-10-08 04:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dee8bad-d762-3a77-8faf-bcb531922024 | -13.39147 | -61.93446 | 2024-10-08 04:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb320780-2685-3403-9b32-4b2b2435f285 | -13.39503 | -61.93953 | 2024-10-08 04:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 737c0eaa-f3a7-3735-8a07-d974fd97ef1b | -13.38791 | -61.92937 | 2024-10-08 04:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0932f141-7b8f-3ebe-805f-75c8c05d168c | -13.38713 | -61.93361 | 2024-10-08 04:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d10ba39-fda2-3ac8-bd70-3b5646f2d893 | -9.28186 | -62.32492 | 2024-10-08 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3222e8e-4574-37b5-85fd-2ccd76217108 | -9.16387 | -61.57058 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4de5d706-ba69-3147-a964-ad0f1adef38e | -9.16305 | -61.57526 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6fefc2c0-8cc9-3a78-bc48-7cf2a9623b43 | -9.15931 | -61.56977 | 2024-10-08 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27d154fc-78e2-3edb-9838-24858f7c6fd5 | -9.1232 | -61.42986 | 2024-10-08 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README89.md)
