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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a5d1a96-6059-3a76-a9c6-84b03dd51f58 | -1.5852 | -48.02951 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ded7141e-8373-3d93-abb6-2eaae60b44d4 | -1.52596 | -52.20546 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 774918fc-6022-31e8-bf48-ef3adce85b59 | -1.68516 | -48.04135 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfe9daaa-e36a-33f7-9c71-a8855d716f05 | -1.681 | -48.4781 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9b5186-ffec-3d10-9792-250ac9b1cbdd | -0.30409 | -51.70446 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb54186c-4e19-3590-9370-38e4b6d70140 | -2.30153 | -48.55416 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec52a87c-be19-3fa3-9ccd-090c0047436d | -3.00283 | -40.28176 | 2024-11-10 04:36:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 520dc1a8-81ec-36ed-85d3-ca624ac86a4e | -1.52217 | -52.20486 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a91082c5-cb61-392b-8bac-630d3b222cae | -2.37654 | -48.56981 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc56beb7-ee85-365a-a77e-979da566e031 | -1.052 | -47.89304 | 2024-11-10 04:36:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50d70afe-7192-312b-afb4-162c158360dd | -2.36596 | -46.87464 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629f5054-6981-386b-9502-b6ccef044abc | -1.20564 | -53.63115 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a26b791-d649-3821-8629-df0a54abdb39 | -2.23095 | -48.48664 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2767c5-d22e-30f5-9bc7-a14741711ca6 | -2.37618 | -46.80942 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e21b633-4b22-329e-9763-683f290af8b8 | -2.62565 | -46.77613 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9e9eb9a-ed4e-3203-93e3-29e559a1f76e | -2.08336 | -48.26271 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 410f5e21-47b6-355f-a5b5-02730cc73c66 | -1.16889 | -52.09397 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26db299a-515a-3f5c-b181-b95674c8cf9b | -2.35008 | -46.66344 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44bb9f1c-855c-31de-9bce-7afbcf3dccfe | -2.56259 | -46.53313 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7706a6c2-4ebe-344d-a6ba-dcb5a76e955f | -1.61186 | -48.6794 | 2024-11-10 04:36:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99939bee-0e57-35f6-8a46-51a8fce1e519 | -1.22642 | -51.75925 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ac6a235-953c-3eb2-b271-8d9538d27feb | -2.40115 | -46.78347 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d325dd0-7342-3fef-9319-5c33ea2b4299 | -2.40976 | -48.40206 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffed2343-6eb8-3f32-8c91-870d4f086646 | -2.20849 | -48.37026 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 209f5cd3-6208-3ab5-ae0c-e63fefc80d03 | -2.21627 | -48.38558 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34ef7f48-715f-3fc3-b436-398b88b7b732 | -2.19577 | -48.36475 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b264a9e-42d8-3fe3-8210-2f6e01d11124 | -2.06664 | -50.90339 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76b674a4-789c-37a0-8c55-65dabeed3866 | -2.30214 | -46.72379 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d25d71ce-b367-31e2-b236-1efaf987cec9 | -2.07812 | -50.33842 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f2d460f-850b-3fae-b0e8-a1332be00bf1 | -1.44924 | -51.67123 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f887617-55c2-37b5-a58a-45fafe5c2e3a | -1.17646 | -52.09517 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a72bcccc-5e79-3e35-9587-630d3b891393 | -1.20444 | -53.63881 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fff3c98-2ada-31f5-80cf-686abf08c934 | -2.21313 | -46.80301 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8af6c4ac-7fad-3ed1-a080-685e55d99e91 | -1.32038 | -54.6386 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 06954c69-704e-3364-8bb7-2a74b2e84381 | -2.15986 | -46.67547 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87d5c14b-aae1-3a07-b1b5-b46c7b1f8df3 | -2.68223 | -46.79236 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d1f6da-4854-312a-9693-bd9cf4e28cf8 | -2.40641 | -46.29927 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 742af9a3-5c4f-3226-9dc8-af7bece84375 | -2.11801 | -48.38804 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| effc5799-f321-35be-81b7-5280f2326967 | 0.28259 | -51.26059 | 2024-11-10 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd009cd1-5494-39e0-b123-a881cb989f65 | -1.20187 | -54.17335 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eeafc18-a1ac-3b1c-8b00-a0f699a8d83b | -1.48547 | -51.75234 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93d4f233-942f-3a0f-ab8e-dd76615730b3 | -0.85539 | -47.6364 | 2024-11-10 04:36:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26c544a6-3a91-3833-8b77-943b94440c94 | -1.62118 | -50.68878 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55365160-4ede-3791-a091-0488651db0be | -1.6422 | -53.3847 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e16bce5b-2907-3259-8162-9a703de2745d | -2.06807 | -46.08231 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c47bcf3-ea08-368f-9d72-112c4aa1267c | -2.33404 | -48.52039 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90bdd507-f042-34e5-9a85-3ac239dbff7e | -2.35064 | -46.63724 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83096d15-8743-336b-84be-f1ce594ecde9 | -2.34824 | -46.52018 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b33448a8-0daa-3ba6-aaf7-407ba1c01cf5 | -2.33946 | -48.48595 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed05c8f-e2eb-38ff-8dbc-13126ec57683 | -2.57298 | -47.3381 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2596e4d2-b48b-3cf1-a796-4ce836811c97 | -2.24112 | -48.37886 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dbfa746-8267-39bc-82ca-74c20d24f358 | -2.1112 | -46.47292 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96a38fac-0c8d-3cc0-9fc4-b82dfb689440 | -2.625 | -46.13729 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0454ab74-4caf-3e06-a875-6d218b7c04c6 | -2.9017 | -45.56676 | 2024-11-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2fba97d4-0578-3d31-ac83-ad6ab80c9bf9 | -1.1963 | -53.69069 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdb64f25-fae4-3448-a6e0-256d2c142ecd | -2.08844 | -48.29525 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10f4f8d4-7b94-3976-bec0-870c5e62f75f | -2.12034 | -46.48183 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 314237e0-a2bd-3300-8926-b925f06d2ac3 | -2.35089 | -48.92659 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa1fa320-ffbb-3b44-943c-b846b7059948 | -2.68337 | -46.78505 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62d1c7c8-fcd7-30c5-9024-8135164d5b60 | -2.14897 | -48.83437 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a46bea8c-a366-3db0-b0ed-fa13d06ea8f5 | -1.16575 | -51.91964 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71d39783-78d4-3d6d-a599-e1bdd10f6abd | -2.40513 | -46.78035 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d1fe3a9-67f5-326f-98ca-c47f2000e621 | -2.16222 | -48.38786 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb5d8c0-4f32-3612-9cfc-4378b33636bb | -1.20262 | -53.62319 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de920d11-93ea-3eee-afee-e686af6cd0dc | -1.63466 | -46.08444 | 2024-11-10 04:36:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aaf22ae-94d7-3fec-b7ad-0e1952d92e5d | -1.90821 | -51.50745 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4fe2189-0d35-3091-a46f-1d753c1b6e93 | -2.11578 | -48.38064 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f361f8-b53f-37f7-be66-01c08a49c378 | -2.31571 | -46.48103 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bcdd0af-ad80-3e53-81e8-a0b04e21e1bd | -2.63566 | -46.80013 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0222a9de-cff5-3fb5-a5e4-d289a8f87578 | -1.91584 | -45.60316 | 2024-11-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 326d7706-7db7-309d-9c0d-7a8ed002323e | -2.50749 | -47.46121 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e22bec87-997b-3a8e-9479-f100ad663f8a | -2.33458 | -48.51695 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f375cae-e288-3204-847e-a98278b5095a | -2.19149 | -49.12189 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb4d900-6d8d-34b2-b62c-745bec5b9e97 | -2.0656 | -46.3362 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2864d0ea-e40d-3e57-a975-c172fd9cbfd9 | -1.25549 | -48.32011 | 2024-11-10 04:36:00 | NPP-375D | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c455983f-bb27-3a7c-8fe9-908892eda605 | -1.37794 | -52.25982 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd32f85f-c8a1-392a-a86e-1e7d997e37e4 | -2.89875 | -45.56211 | 2024-11-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be4f5b13-8afe-303e-972a-69c217908f6f | -2.17634 | -48.33703 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05c15fac-3e9d-3ef7-93cc-35e1c2fb9b3b | -2.17044 | -48.39608 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d806a38b-3b80-3a40-b6ae-e5e1b1f0932a | -2.06905 | -46.33673 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aae1bb1f-0823-3c46-914f-7c465ab3412b | -2.40121 | -48.49954 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d97d114-ddb3-37cb-9867-412c0df5b167 | -2.62849 | -46.13783 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f80aa77-4e8d-3e21-8865-cd9a70a19354 | -2.12463 | -46.38734 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241f6dae-b922-3264-bd22-12573eb4c2b4 | -1.53661 | -52.21186 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 103ff0c6-093b-345f-9462-492d0c300a0c | -2.20179 | -47.7467 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392fcecc-435e-374d-9891-ad3c744fa302 | -2.12092 | -46.47815 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 388cb75b-b740-3c3b-b911-a7d55f099843 | 2.42519 | -50.77652 | 2024-11-10 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc66093d-e9f9-3b41-9afc-0395c0393bc4 | -1.43 | -54.54074 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eeaf8d7f-017b-3e2b-80fe-aa041d841c6c | -1.59539 | -52.75183 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 725ee1eb-4e25-34ed-97fa-3072771806e7 | -2.33755 | -48.58447 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25aad8cd-6758-3f81-8989-fabb81d9ef77 | -1.42147 | -52.28107 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b392d255-8c58-3716-8710-9a1ab3372d9d | 1.62076 | -56.05165 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c73559c3-d065-3c10-809e-4a11a0d61af4 | -2.672 | -46.79081 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e03aa7c7-89d1-321c-a5f7-2f10a5247fe4 | -2.42718 | -46.30247 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21de4c78-3e36-3d35-981c-5bcf5b4c40b3 | -2.62667 | -46.14935 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8b410eb-850d-3723-bf6f-1b04ddba646a | -2.50735 | -46.27537 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee1b0d0-f87c-35ad-9c64-9ddd6db6a740 | -2.13657 | -46.69057 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 070e631a-996e-3268-9feb-ebe3bda34eb9 | -1.23524 | -51.75166 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4080f824-021d-393b-8ea0-92d6b711efa1 | -2.1077 | -45.33606 | 2024-11-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 80da9372-aa21-39df-bc45-27b8ee1b4fc7 | -2.2009 | -49.51874 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README67.md)
