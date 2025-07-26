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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d1a494-3e7e-353c-9f6d-ccc8967cf2f8 | -6.64293 | -58.84896 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 338ff7b7-67be-393b-b547-d0e9bf4daba7 | -6.66256 | -58.85772 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8cc62bb2-bce6-323d-a3eb-1dd03c9af666 | -6.67923 | -58.84929 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1b54cbd3-8393-336f-9f48-ed55c7ae8b65 | -6.61809 | -58.82694 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d435f2b6-1a77-3dda-be76-a7f235d8e2b7 | -6.62327 | -58.84032 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a3bdff83-d6de-3e6b-9c99-4e78afad0aaa | -6.63608 | -58.8483 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 97451f17-13fa-3c7c-8640-a2e2805c56f4 | -6.61434 | -58.8448 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94825071-eafe-3606-aee4-e9a380845dc9 | -6.67397 | -58.83625 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c45ed888-e40b-398f-b4b2-74d56491f3df | -6.64213 | -58.85498 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| c254cc65-2154-3519-9d33-35227ce77c18 | -6.64027 | -58.81679 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e69c9398-2c00-37f3-985e-0d96591892e4 | -6.67866 | -58.84126 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d4566ada-907f-38f4-96df-7bd0af8b036d | -6.65822 | -58.83839 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 2833fa3f-471a-3998-a65b-123c94d3ac1d | -6.63423 | -58.8099 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a7129f8-2dec-312e-9941-377aac5f58b9 | -6.62089 | -58.85832 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f3384583-8c05-3bb8-a5a8-bff0d2372941 | -6.68242 | -58.82454 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d36ae03-307a-3a8f-9879-d9fc604a58f6 | -6.6446 | -58.83645 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ef7db28a-dc4f-3bcd-bd7a-29e09fde9a20 | -6.61567 | -58.84536 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b7c1217a-bcab-395c-a784-b46ab1eab01c | -6.6189 | -58.82083 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7a6703a-809c-3302-85a0-0867fae72da9 | -6.67785 | -58.84726 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d8a138b1-b40a-3bc2-8c5d-24c6c91afb75 | -6.67184 | -58.84034 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 7f3617c0-f0cd-3c15-9b1c-594a1fedc2a3 | -6.69366 | -58.84504 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ec26c1a-cf43-39cc-91c0-0ace0a7f319c | -6.65224 | -58.83119 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9830a5de-311d-3671-ac94-252a7ce54534 | -6.65988 | -58.82602 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| e76ab309-054d-3e83-a8f3-4c0e7216df82 | -7.29348 | -60.1752 | 2025-07-26 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b951370-5a17-3c04-bd8e-ff87837e7c9f | -6.66403 | -58.85974 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 93e0597c-0458-3a9b-81ec-0a723927abea | -6.66795 | -58.82902 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fbc6b552-3836-30aa-9498-90dffb4b848c | -6.69148 | -58.84903 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e1d1323a-213a-308e-becf-059d13cea9bc | -6.69287 | -58.85107 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd4477b-a144-30ee-99a1-a13bac5f641d | -7.29281 | -60.18029 | 2025-07-26 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97ddade0-94a5-3ff4-81de-3b49c7684da2 | -6.6876 | -58.83821 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0469a32d-1790-3ef0-840c-ccd1acda6281 | -6.65141 | -58.83742 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e40ee055-a784-31e7-800e-2c4faddbad2d | -6.67351 | -58.828 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3b79659a-51be-3ef1-8596-a07fa760947e | -6.6277 | -58.85925 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0eb25ec8-334f-3f8d-93ab-a155195b4a1c | -6.61773 | -58.82032 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7667ac26-4e3b-38ba-a94e-8f4ba0aad3d1 | -6.62656 | -58.8154 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d30bec-9633-3b53-80c0-a0165d05dcb6 | -6.66586 | -58.8332 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7f3a30e7-3dce-34e3-889f-bd5eb83300cc | -6.66637 | -58.84138 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0ce3c7c4-1dc7-3f33-a2c7-0dbf06834650 | -6.64375 | -58.84278 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6653e635-2b2e-315e-a400-1387adf3462f | -6.62247 | -58.84637 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 406b5848-9632-38b4-8631-45a9539e8ab7 | -6.67701 | -58.85341 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d94e5e60-a1a7-35a8-bac3-7743c5be28b3 | -6.6724 | -58.84846 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 029ffda9-eb84-322c-ad34-626805c08e0f | -6.63091 | -58.83504 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 1b1f3241-49fa-3325-a72f-d126e9803951 | -6.67267 | -58.83421 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fea1613c-e6bd-3afb-9c3d-91479cd18f07 | -6.64626 | -58.82395 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b0860dfb-44ff-371f-89eb-990fa86996fc | -6.61729 | -58.83308 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bd940541-ad22-3619-a4e7-273819d9f34e | -6.67319 | -58.84234 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 08298bad-201e-34ac-90c4-b361597733ee | -6.67082 | -58.8608 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f3151837-9181-3e10-b09e-8d7d345bfabe | -6.66876 | -58.82272 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| eba3e123-4593-38a2-9aca-ee9c0108ab54 | -6.64894 | -58.85588 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 37ad0d0c-c110-348e-92aa-6785d96e8ddc | -6.65307 | -58.825 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0a564c82-569e-3b93-b741-7b228eee81a4 | -6.62738 | -58.80918 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a972fa19-7ab2-3422-859b-d7ce1b99f77f | -6.67102 | -58.84646 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 56d90f90-f72b-39bb-a21f-cf046bc57bba | -6.62848 | -58.85338 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6a521e7b-b695-3b47-b917-9d76631b7f50 | -6.62168 | -58.85234 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c3c18db8-67b7-3d3e-b532-5b16e9070054 | -6.63775 | -58.83577 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 2962cce3-9f18-340c-8c56-818ba1e5ff99 | -6.65905 | -58.83221 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 21f1ec7c-6296-3735-a7c7-969abc2fa886 | -6.67161 | -58.85463 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4c72d897-a4e1-3022-a5a7-4a23d2103ac8 | -6.61648 | -58.83923 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2704830d-abda-3e12-b2c7-ff7385e945b0 | -6.66716 | -58.83519 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4c1b8060-c6d9-352e-8b65-209aac5b9fe5 | -6.68604 | -58.85025 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| aa35c3e7-3550-321d-833d-e4efd5d619fe | -6.61689 | -58.82641 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cd469c5-8d5d-3147-986a-67b628012aa4 | -6.63945 | -58.82299 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf524805-cc45-3749-8b76-33c5d4898a60 | -6.65575 | -58.8568 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| adf4e3a7-c4a6-3fa0-b6b7-93826494724d | -6.68383 | -58.85428 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d47eac24-3ff3-3302-9e70-71cc580f537e | -6.68683 | -58.84419 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 57da2f94-8ffe-3724-8ea9-1bf95ea5aa0f | -6.6369 | -58.84219 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 49678da1-f9d0-307a-9af8-04cee80038ea | -6.62575 | -58.82154 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1840d85-25e3-366e-994c-9603b9521aee | -6.66337 | -58.85167 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3fb0947b-4afe-3d3c-ac4c-534f9d35a4d7 | -6.67476 | -58.83005 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 59e08778-565b-37be-b65e-ca847787cda8 | -6.62492 | -58.82787 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 33626cf0-a2ab-361a-8607-f8f720149cd7 | -6.64975 | -58.8498 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 81dbe2f5-ead3-3e63-a9e6-66fa2841d105 | -6.68078 | -58.8373 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 807a5c1d-48b2-36fe-89c2-8bd45ef20291 | -6.65057 | -58.84367 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| af9e9db4-bcdc-36b0-a5ac-0ef3643df788 | -6.66936 | -58.85875 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a65842c3-1cee-3c5f-961c-abaf7566d2b9 | -6.66558 | -58.84756 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| eed2c3b1-7ff0-3484-a676-026ad7cf7538 | -6.66419 | -58.84558 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0dddb7ec-c05b-3e58-bcc0-379bdb203868 | -6.63861 | -58.82928 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 7f686b7f-121e-3902-b239-434688c7935f | -6.64544 | -58.83015 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 63ad644e-d8be-3171-b633-4c579e0d3cca | -6.68547 | -58.84218 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1b3f65ef-d8a6-3de2-bb71-2a2b4589cef5 | -6.67019 | -58.8526 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ef965a73-529f-30a1-8f1d-ace732f81584 | -6.6326 | -58.82221 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 283c9617-e304-3aae-ae24-81dfad4776fa | -6.67844 | -58.85544 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 2b6cfe37-0253-3eec-85f2-59752a0eafbd | -6.65738 | -58.84466 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ada518b3-6c28-3217-b781-d9275fe434ec | -6.66503 | -58.83936 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f6c1e199-b7bf-30b1-b7af-288b0ba393e7 | -6.63176 | -58.8286 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 94775919-cc8e-39e6-b016-c773d1cfc2fa | -6.6648 | -58.85366 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 67449687-8f85-327e-be32-4ab5fc0588e4 | -6.63531 | -58.85415 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f4bcd910-1bb0-37fb-822f-d97a89e10736 | -6.65656 | -58.85075 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 539c0f5d-906f-3720-9ede-a8d55983b6dd | -6.68158 | -58.83105 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1cd1c9bf-81e0-3dbf-923c-f7736d85a484 | -6.66669 | -58.82702 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 7db0764a-ba2f-3462-b9fa-ae0f534702b5 | -6.68629 | -58.83617 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d58daaff-8775-32b5-a393-0fabba59829c | -6.61604 | -58.8325 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bb66774-2f0c-353e-a16a-27afd784da1c | -6.63342 | -58.81604 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c910522-0531-3f17-907a-f7e4440dae3c | -6.67947 | -58.83525 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8146d918-e034-33a4-afc2-1bb384e636f6 | -6.63007 | -58.84136 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 7aecd239-b6b4-32f3-845a-fe23bfaba21d | -6.61519 | -58.83867 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffd413fe-e3e9-39e8-8c34-3d88b0121021 | -6.68032 | -58.82898 | 2025-07-26 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8d911b0c-c745-389e-90e4-bae1caf1aaf3 | -7.66078 | -69.9306 | 2025-07-26 06:08:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e8f3e32-b0a2-3ff9-84fe-41a794dfb05d | -8.09419 | -61.40192 | 2025-07-26 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a83ab9e0-8d74-3390-b2a9-6b7507d65e1e | -7.49289 | -63.82177 | 2025-07-26 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
