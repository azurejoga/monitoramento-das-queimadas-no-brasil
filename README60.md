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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30d93555-c0f9-3791-9e7c-c8a112ad3d03 | -2.67427 | -46.70859 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29f26efc-62c5-377c-95b6-981941f26cb0 | -2.39524 | -46.50803 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac7f089e-f7e3-3574-84e3-1e536989bcd1 | -2.30303 | -48.50145 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0010ab63-7749-36f8-a034-2295090bee8b | -1.766 | -45.6129 | 2024-11-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abb14cbc-0400-342c-abd2-6e32896f677f | -2.05384 | -47.7232 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f25e08e0-8b63-308c-9b4c-b334520c8548 | -2.32191 | -48.53263 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e234751-263b-3ee7-842e-40d685e103ca | -1.94222 | -47.35209 | 2024-11-10 04:36:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 086b1bdd-fbc8-3c5e-be2a-048f52ce563a | -2.35065 | -46.65978 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd8134fe-a793-3fbe-952c-08be1b1b414a | -2.3957 | -47.71602 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 616a94ba-d645-36f0-95cf-90c55265c4a2 | -2.19397 | -46.85938 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d34a9fc3-68bf-389a-b85a-e37ea8feda40 | -2.11809 | -48.90047 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4519354c-58fc-339e-a588-345716def455 | -2.14189 | -49.13914 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f7642dc-1f5e-3365-8a2a-6e1913482767 | -2.15011 | -48.84872 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aaa48287-4e76-3fc6-9119-93fd51c94617 | -2.49745 | -46.3856 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 711381b7-5d00-39ea-84db-7373947fb0bb | -2.62485 | -46.16087 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5774358-d7c8-33b1-9475-2d468feaf28a | -1.28219 | -52.20853 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f395c4a-4873-3702-a8e8-b15df14be6e7 | -1.5191 | -52.19967 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 72a832fc-5a5f-3363-a099-af8d7ef68088 | -2.42471 | -45.54819 | 2024-11-10 04:36:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 09dc3fd2-7ece-31ff-a575-4fd06a0cc65a | -2.38979 | -46.78922 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45dff58b-237b-3759-9e1f-3737b2fc4856 | -2.50905 | -46.31038 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 321abb6a-4b3f-34f5-ae5c-c0ddff35e373 | -2.29562 | -46.51967 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61b9c4c7-024b-3e52-8a7f-19d7c0d0650e | -1.98174 | -49.01448 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38d7a7e4-f7f4-386e-bd23-97422040f86f | -1.25099 | -51.77209 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ab5988d-0329-33fc-9d70-ea62a5dab462 | -2.23055 | -46.62282 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5bfd4c4-bcd3-3941-b031-f146abb36204 | -2.14494 | -50.27277 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66b2d84-4d18-3504-bf88-7476afda85c8 | -2.50639 | -47.46824 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3bd0ad89-ed32-3db3-94e5-739d3da7dc32 | -2.20059 | -46.79345 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57c5ab61-5db0-39ba-b698-07fc027cbfb9 | -2.39627 | -46.59153 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13525c24-41b3-3d66-9c98-e92efa3ecb02 | -2.209 | -47.74426 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc47fa9d-e8df-3fdc-b0d2-b015c8bfc2cd | -2.08389 | -48.82083 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07f91420-cb54-3122-8546-930bc93cbd9f | -2.67995 | -46.807 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 991d4d82-e4fc-3e4c-8d61-55e7ea85d49c | -2.12807 | -46.38787 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d66452c-8b0b-34d6-9a45-bd5afb968688 | -2.36186 | -48.87866 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c76b1b9a-94ef-33ac-8a07-d20e80214f9b | -2.22761 | -46.42168 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78dec917-efcc-344a-8e28-38bd796e13e9 | 1.62223 | -56.05269 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 046e3f3f-58e4-349d-a76e-897b2eb20a9c | -2.18291 | -48.31688 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eabfbe9c-a540-3640-aeaa-bb38cbc43100 | -2.12154 | -50.13312 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c42f1eb-2a0b-392b-a5cf-ebdf5ee80194 | -2.29266 | -48.54573 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daab1263-38aa-335c-8ff8-15753e86d2a1 | -1.98786 | -48.74199 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7781ccba-0352-3eab-925e-78df167438ed | -1.22377 | -51.96795 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be69cd43-855c-3a90-8f23-da9de5ff5d32 | -1.31441 | -52.25163 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27c30009-efd7-3d31-8112-8ae2d682396a | -2.20845 | -47.74773 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8ee192d-eb14-309b-941f-b905a38adb13 | -2.46243 | -47.93654 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf614ab0-58ca-3b3c-9734-1a2ed67677ef | -2.66632 | -46.78244 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 623286c5-c4ed-3295-b22c-62c75adaa936 | -2.05876 | -48.95889 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6fb07b9-b98d-3822-bd2f-67aa4b3040a4 | -2.29871 | -46.74564 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cef4794-b45e-3e51-949d-e094f30c0528 | -2.46736 | -48.44632 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 819647e9-a768-3051-889c-05bff18b07b3 | -2.34893 | -46.62569 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 410b8de9-7997-3757-9e73-ed1d8a249a6c | -2.19691 | -48.37904 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14002a07-8740-30ea-9feb-7e94616875a3 | -2.11246 | -48.38012 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dadb6ded-83ae-3b29-b0a7-b936c0d7e89d | -2.62788 | -46.14167 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 467cee55-fa1d-3931-8d57-cb1bf5cb9065 | -2.10222 | -50.74585 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b9194d3-c093-36a0-91a5-fcd322a6d43c | -2.12794 | -48.56247 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98a8e9b9-bed3-3086-af15-357edffd2756 | -2.3997 | -46.59205 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25bbbc40-4835-3bf0-b6d7-98fb1dd483ad | -1.72855 | -51.1654 | 2024-11-10 04:36:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d474cf78-6104-3a76-bb0c-79fa983b1a56 | -2.62622 | -46.7725 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 57330af1-ffb7-3271-b1cb-c4a11394d7ee | -2.34724 | -46.68174 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc3deceb-294f-3d60-9a52-72722a9aecf7 | -2.29211 | -48.54917 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a618f19d-bbe5-3dd3-8685-b8b0fb9afdf3 | -2.68393 | -46.80385 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe932d50-5853-3f87-b107-2323c8145153 | -2.15213 | -48.34396 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1fa170c-7d69-3556-9a85-0f8310493a9b | 3.37148 | -51.27183 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a757462-6f69-3ba6-a008-588e70f1b687 | -2.0691 | -50.72879 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec9b669-88c9-31de-aee6-ae3c0f4f29dc | -1.50614 | -52.1835 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5175862f-2508-304b-9c51-e70464bc4219 | -2.41122 | -48.52227 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 232a9c77-cc75-3e27-aceb-35aa1538ead0 | -2.36087 | -46.79593 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ca6878a-166b-3a83-b4a9-8304db126f4c | -2.63679 | -46.79284 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21ad63a7-2240-3ea5-81d8-97b24773d3c1 | -2.40066 | -48.50298 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30663b9b-4163-308c-bab1-968079e66b88 | -2.37084 | -48.9297 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8c926d-a78a-36a2-9b27-51393380677b | 0.64427 | -51.91589 | 2024-11-10 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45027ec1-24ec-3e0f-aa70-b52e9d4e2129 | -1.23131 | -54.1552 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0513afb7-fa8d-3532-99ad-34e135e9ddf6 | -1.3936 | -52.06501 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6aa203fd-99cf-3cbe-901f-b1dda587c5f3 | -2.44212 | -46.32023 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dddb23b-89f3-3729-a6a5-49a123161557 | -2.12331 | -49.01859 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8076648-a1e6-32de-a3c4-3e7d89e2215c | -2.15247 | -46.70044 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d3e98bd-eaa2-343d-a821-1203ae524895 | -1.49884 | -54.39271 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7aa086db-57d8-3bdf-9a81-3d0978f4714f | -2.22387 | -46.53499 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c486db9-4def-3e08-8eac-bca73087447c | -2.36765 | -46.86383 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5e5f18b-f901-35c5-ae49-f836af9fb260 | -2.20572 | -48.3663 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e9d9b290-9f8a-3ba9-9378-a40455d7ac6f | -1.98459 | -46.43476 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7d11fa9-c2f9-363c-b708-61f0266b1d56 | -1.68635 | -50.41322 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b08a182c-c4bb-3066-b52c-389958de3ce0 | -1.21318 | -51.77063 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d8bc2a8-5193-3a9c-bc61-edc51f688e46 | -2.2439 | -48.38282 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7853f3a-1341-3aaa-ad1c-870aeff717bd | -1.15028 | -53.65637 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f575eb15-1f81-38a9-bfb9-c58a63b3dcd8 | -2.2827 | -48.54418 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b83b9893-333b-3da0-8eb1-1b5ec38f8755 | -1.67301 | -53.14044 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07cc3073-19f7-3310-89ea-bde4af2f15ed | -2.2049 | -48.84316 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 461078cc-f02e-3de7-9eba-73a1f94a5474 | -2.24387 | -46.36308 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00e4ef92-fc17-36f4-91e6-34d59482e5c8 | -1.4904 | -52.55637 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3575e175-b081-3f6a-93a8-a66c49431077 | -2.05051 | -47.72268 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09d3cbe2-7eac-3b18-bdfe-c6519ddb2cd8 | -2.67654 | -46.8065 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0016d369-2ee2-3283-a158-1f19d5a36264 | -2.67598 | -46.78767 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6c62b72-6b44-32a9-831b-06fd90f53483 | -1.39288 | -52.06953 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9d79cc9-5604-3467-a0af-4f37f7be4060 | -2.2953 | -46.74512 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3b6b0c2-2f99-3c34-8d4c-944d067c2002 | -2.28442 | -46.85853 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8599c5d5-4702-353e-8677-f26da74b5565 | -2.20094 | -49.12693 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ba66ede-5ced-38ef-bb02-87c6076b87fd | -2.24426 | -45.53067 | 2024-11-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c12a09e-9cf1-3cea-9852-55084c75dd8a | -2.52973 | -47.38535 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 451ba4e6-1a10-3a01-8073-b301cb30aeaf | -1.51531 | -52.19907 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ceed036-b50c-36dd-8915-bcb28af70f55 | -2.10853 | -50.6603 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d2a2e93-0f45-3b90-aa77-4b5e0428b757 | -1.67066 | -49.9622 | 2024-11-10 04:36:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README61.md)
