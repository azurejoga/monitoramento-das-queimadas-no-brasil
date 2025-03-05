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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 629d0abc-76ae-375a-87ed-ca27be5d9deb | 1.12978 | -60.51344 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ed3468f-85cb-35a4-a2e1-3e44a43c187b | 2.62278 | -60.41454 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53afa8e4-8ebd-32bc-ab34-553bbb3949cb | 1.16593 | -60.10004 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a7d9397-0258-3246-aad8-79e70af52b06 | 1.94323 | -60.37823 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59c448ae-92ad-3462-ab90-bce6e5866be4 | 1.76864 | -60.21926 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1c1def9-5658-30d8-ad1c-4968265463a7 | 1.50536 | -60.19358 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14cc9bf5-00c0-3fda-80f4-bb0e6c516acb | 3.34039 | -61.24627 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef5fb57-07a3-3539-95fd-28957a29bd31 | 1.02563 | -60.38145 | 2025-03-05 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4357714-5692-31d9-a3fb-360d0f20758a | 2.35553 | -61.00585 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37482c2c-6a42-35a1-8769-bab36fbc4ddf | 2.86303 | -60.74688 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5681c71e-e6a7-3185-bf9a-427440167b4f | 3.34396 | -61.24569 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a189a6a-22dd-30c3-875f-e3c5f500c9df | 2.35042 | -61.06519 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4769470-3546-3e6b-b585-648d9c830bab | 1.57539 | -60.99712 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92a9bf74-fdc9-36a3-9292-c68962dfccb5 | 1.5048 | -60.19004 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 661050ca-67e4-356b-b3a5-1643d995d28a | 1.1326 | -60.50927 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a77f9859-5b63-376a-9986-0d77c2be2afc | 1.16125 | -59.15067 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bfa848f-8563-3a2b-b7bd-f4a76c520ee6 | 1.16788 | -59.14964 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4aafcccb-6b25-37ff-89e4-cd1453128e44 | 2.77711 | -60.8886 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b29bb14c-6881-3be9-828f-fb686e2fa283 | 1.1292 | -60.5098 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a872d91a-188f-3559-aa15-23fc8cf8feb1 | 2.26656 | -60.2577 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cd10549-fc60-314a-8c09-61fbf07b42d7 | 1.95287 | -60.373 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d441d05-986b-3622-aa6a-6daa7aab6fcd | 1.17892 | -59.15498 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96df7c88-c80e-3963-b451-a1ffa6ffc24e | 1.18223 | -59.15446 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b151913b-15f1-337b-86dc-542fe99b75e4 | 0.97478 | -60.37056 | 2025-03-05 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e93cb38f-a3bb-3955-8c87-3accfba6f1bb | 1.64795 | -60.29686 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad51d28a-b312-36b8-bdb2-275f56fcef92 | 2.77422 | -60.89299 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c849cb7-268d-3d94-b5ce-7afd68bc87ac | 2.10755 | -61.26559 | 2025-03-05 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca612b43-4cf6-316e-954b-50e8f2e617e6 | 1.94266 | -60.37459 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80a068fa-da34-3dae-aeef-9c41b10ab31e | 1.08572 | -60.6774 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f50d39de-dcb5-3bb9-9ed2-278133129d1b | 1.93869 | -60.3938 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf006e17-b5d6-3eda-9388-126532205596 | 3.23629 | -61.19976 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6a6adfc-9b82-3402-ab54-f5abe12111c8 | 1.136 | -60.50875 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 287bf502-aef8-32bc-92f7-5009d1c7e197 | 1.28146 | -60.08179 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 147833e8-06db-3f50-bb92-02d334cdc1b2 | 1.08231 | -60.67794 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0274785d-c99d-37e3-802c-7148b0f0c7ce | 2.35564 | -61.05262 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8571e5a5-33e9-37b7-b2a9-a9c6e9bce6e0 | 2.35742 | -61.06407 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56b33a40-cf57-3d58-93f5-47e5a5fd2ccb | 1.13035 | -60.51707 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5253259-cab8-3b4f-8463-3e13aab49956 | 2.77651 | -60.88474 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99db251c-814f-3560-8360-fc2660be4792 | 1.90131 | -60.57574 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e279f1c9-876e-3943-bf31-516adedcc806 | 3.31282 | -61.20912 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7f74505-f92e-30f3-8870-507f92f9bc5a | 2.39533 | -60.23462 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c533c2e-67ba-31ea-be04-64aae6962884 | 1.13658 | -60.51237 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb197544-7277-3bae-95af-0329c40403b0 | 1.1712 | -59.14912 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74537bfd-8f0f-35aa-8af0-6ea8669e1135 | 1.85678 | -60.58268 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eaa66f7-90b9-33e7-a3a1-736e1f66afef | 1.7692 | -60.22287 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd53a136-48f0-3d99-b98a-597884335824 | 2.39585 | -60.23481 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c98c4264-1309-32bb-aa86-84515151427b | 1.93643 | -60.40165 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c103f6c-4dc2-3b0e-a51b-1bb43b0c4a60 | 2.35854 | -61.04818 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6641120d-fa80-3e44-a8d6-5e94dfd7163b | 2.51986 | -60.99437 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5d495066-91fd-3d66-9dc4-6a71bc4cecc0 | 1.17837 | -59.15154 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74adf1a-0279-3dc5-aeea-790c19fa4f88 | 2.35261 | -61.01014 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 368b239a-b9a7-362c-9551-a09d8b41645d | 1.17451 | -59.14861 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6889097b-3440-344b-91e1-3a7c5cd3dc61 | 1.94946 | -60.37353 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 069e176c-5ee8-3e42-8a3f-79790128470c | 2.20826 | -60.15184 | 2025-03-05 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9db8cc-d759-36c7-acbf-a1d3c8b90758 | 1.1258 | -60.51033 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10f56d86-fc0a-3879-ae63-2a36336c503c | 2.51577 | -60.99105 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7806d01d-8f27-3f87-9c55-c1e0f32d9273 | 2.6262 | -60.41401 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a394070-e574-3d2f-8ed7-7c0eda8f4833 | 3.34815 | -61.24919 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 799f3e65-737b-31f5-b114-406727a27e7f | 0.63251 | -60.00912 | 2025-03-05 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 773f9279-9605-306c-803d-1bccc53fc9f3 | 1.30874 | -60.40787 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06886492-6886-39e6-9110-c38ac64f8cf2 | 1.08174 | -60.67427 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4be3a040-01e9-3796-8af7-75018657344d | 1.94606 | -60.37406 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8492854-1aa0-3cc5-be3e-014c78d6b516 | 3.08301 | -60.07483 | 2025-03-05 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12628a2f-020b-3431-b078-2807f425ef3d | 3.0388 | -60.10402 | 2025-03-05 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab79a9d1-9f64-3b6a-9e0f-b5c4319c2133 | 1.08515 | -60.67373 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67ccf487-fc4c-341a-aa90-18d2012d2a5a | 1.95004 | -60.37717 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16c9d320-ef5b-3f2a-aaae-27bd239b4166 | 2.37152 | -60.2382 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e769b020-d440-3a68-95bf-2a1f4208c5ad | 2.85955 | -60.7474 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9625b2f-ce23-3a16-8036-86fcfeb63f6a | 3.34458 | -61.24975 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed899660-4095-333f-8caf-31d524dce3fe | 1.18169 | -59.15102 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a84decb-353d-35a1-a598-2914a9826ff9 | 1.12638 | -60.51397 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c72625e3-9024-3d01-ac59-88c468c0925c | 2.10297 | -60.2387 | 2025-03-05 05:22:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c59f9ee6-3470-37a5-96d7-3c6d9175bc1a | 2.40719 | -60.24059 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b35b0c0e-ea48-31a0-b1ba-ff2b2f485868 | 2.35392 | -61.06464 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90a0b97a-bd66-31d7-b6a7-3ce4cd9d47fb | 2.35611 | -61.00956 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4526c085-eb4f-3819-894f-89628674e68f | 2.35203 | -61.00639 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fa8443e8-2f59-392e-8feb-2816b102faf7 | 1.16456 | -59.15015 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 13312ad4-906f-3737-9266-4f9e7bbeb92f | 1.17506 | -59.15205 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36546da-9c44-36d2-a391-3c82e6487ece | 0.7718 | -60.41311 | 2025-03-05 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45b38993-a284-38ea-bc31-313c39cf39b8 | 3.23691 | -61.20378 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0123a512-714f-3850-b4bd-a831c8bd3bc9 | 2.77362 | -60.88913 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 20bbd4b5-62f2-3928-b960-dd799f9d8e09 | 1.16179 | -59.15412 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 311b93e5-8188-332e-a3ba-c78166dbfc9b | 2.36033 | -61.05968 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1ad9762-2f1f-3897-8037-64d398b8c76a | 3.31344 | -61.21321 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 871441a2-3335-31d6-9a84-5951349ac580 | 1.65134 | -60.29632 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b643d4f-dc4d-3720-8a93-b55307e8dfdb | 2.34632 | -61.06189 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee6dc2e5-2350-362c-b10d-4e1fa623854a | 2.26713 | -60.26132 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f4cb514-1bb3-35f1-85f6-c5a15ac28512 | 1.16511 | -59.15361 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c371d59f-1d8f-3df1-9c60-0b387e26f51f | 1.12695 | -60.5176 | 2025-03-05 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0d55e0e-7fb8-3adc-a10c-b378bc379929 | 1.16842 | -59.15308 | 2025-03-05 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d8edd98-e5a6-3ab0-ad2e-e180696aa57e | 2.83777 | -60.83688 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cda012b-f452-325a-a4d1-90bb10c871e3 | 1.94663 | -60.3777 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e38a7d6c-697b-3d83-9aff-44fc9c140ef9 | 2.34982 | -61.06134 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 612fe51d-fd82-37c4-a5f5-3588196bd351 | 2.43724 | -60.27701 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dee45e3e-d3e6-363f-af38-9c7a9ec13ad0 | 2.42906 | -60.64915 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc807acb-a628-3e26-935c-12d9cf528130 | 2.86362 | -60.75069 | 2025-03-05 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb55db3e-5f84-3e58-8f34-fb24a4afe0aa | 2.35084 | -60.99877 | 2025-03-05 05:22:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7666fc79-2805-3f2e-a3f8-2d90d9ee14fc | 1.96641 | -60.61562 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52ddaa7-fbe4-3c10-8566-2c5180bada59 | 3.23335 | -61.20433 | 2025-03-05 05:22:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 424bdb9f-dc66-3a1a-be07-5d1961118354 | 2.43383 | -60.2775 | 2025-03-05 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
