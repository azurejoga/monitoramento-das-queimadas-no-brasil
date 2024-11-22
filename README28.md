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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10e7638f-09cf-34a8-8ca5-5945c2816af7 | -6.81699 | -46.77356 | 2024-11-22 04:12:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c68c5b2a-f201-3a62-bae6-42342c99a630 | -3.51115 | -53.80814 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dd5238d-2d36-3d90-b582-a1142ba33fea | -3.80345 | -51.99046 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18af4bfa-4400-38ca-959f-3abf31005673 | -3.88362 | -43.34369 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7c48e0f-0692-3b2e-8d70-13ab4d239f60 | -1.71878 | -52.48946 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a57b984-4781-392b-a4de-68c4cc2c0fe0 | -3.76044 | -49.93411 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa9203e0-ddda-3e46-b39f-b10ab652e0e1 | -4.57389 | -46.59431 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 417c8a67-1bb0-3037-86d9-6486d2901cd9 | -3.49968 | -53.80018 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7fbae86-a024-3bfb-9324-7c810229e83e | -3.46666 | -45.91723 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba9bb013-f343-33bf-9446-4367244723ec | -1.24106 | -51.746 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff82eda9-5d82-3b2f-86a0-f9a6e62b1cd4 | -3.34772 | -42.78773 | 2024-11-22 04:12:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6cbbd292-da69-312d-9047-0646d7e1cfa4 | -3.86404 | -49.90015 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9b1f4a9-9c46-3627-924d-0b7fbc8ea021 | -4.28797 | -48.2404 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79c97775-5de8-3fe3-960a-0dcd331bf7fa | -4.04188 | -44.1544 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 756ca6d1-7541-37ed-a7a6-caa3d620f2ca | -3.25701 | -54.24299 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36383f17-8de3-34fe-b566-de4dd4a1c1f6 | -4.66443 | -46.5354 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e27a9abf-953e-30cf-8aa8-5bc258eb6bb2 | -2.1988 | -53.65557 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36c745dd-04f1-3158-8861-e75794a72e62 | -0.27796 | -51.56417 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0623e74a-ba03-3225-a15d-b79d694b85bf | -3.24962 | -54.24757 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1b2f2dae-16c7-375c-877f-c34f8644dbc8 | -4.54247 | -42.98229 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3039dc3-0df7-307a-a1d7-76503dcd93f3 | -0.30636 | -51.54625 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9895f07f-f60a-32d6-8193-8ebf7d22a4b2 | -2.68076 | -46.16978 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e304cf81-d3a6-3c29-81c7-1142a1c473d1 | -2.57945 | -46.54197 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9a27195-7c40-36ad-b58b-2de1b39ba47d | -2.70716 | -48.66617 | 2024-11-22 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ccf02e5-f811-3051-b378-5dc39615efe2 | -3.28676 | -53.83693 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec7c30b-3937-322a-96fa-d702c6b30ede | -4.58234 | -48.02462 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 205b72c9-6cb0-3a77-b440-1f1b0f9c00ab | -4.00724 | -49.91813 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1234b91f-8150-3c60-9d8b-c0b59fb6ce61 | -6.18773 | -45.44827 | 2024-11-22 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70f55604-669a-3041-947e-14b0fb3ff129 | -12.36087 | -40.40424 | 2024-11-22 04:14:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ae915d0-a857-3575-889e-0244199e98c4 | -7.65764 | -44.50375 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 951526dc-ce94-3324-a294-bdc2964635d2 | -8.3927 | -48.0611 | 2024-11-22 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3f71015-54f3-3d26-bb95-a3efae60e54c | -7.66774 | -44.50538 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4533561f-7c81-36f1-86a4-e4b6f3fa506c | -11.4478 | -39.5879 | 2024-11-22 04:14:00 | NPP-375D | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5aa5df62-b118-3dfa-a0c1-fa11dda545a1 | -7.76039 | -46.22445 | 2024-11-22 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c081bb7-423b-39bb-84a0-d0293c51a1d4 | -7.03319 | -47.63724 | 2024-11-22 04:14:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 280b92a3-8324-3778-9018-51071f31e2aa | -11.83592 | -44.19145 | 2024-11-22 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81bbf58c-4b90-35f3-b357-8dbc2e91db67 | -13.02641 | -43.75444 | 2024-11-22 04:14:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 306849da-fc53-348d-8355-d830dcbc9d7b | -7.68386 | -42.64457 | 2024-11-22 04:14:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 530ab381-4630-3dc7-b07c-4db3b9dc3810 | -9.99678 | -44.73335 | 2024-11-22 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d9c46d6-7253-3edc-8538-632684f8a81b | -8.43123 | -45.79451 | 2024-11-22 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fb8ab11-1072-3c44-aea9-0ec1582b4b43 | -11.36894 | -57.57949 | 2024-11-22 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 169fd56d-5879-3918-8de1-b4fff9cf1289 | -7.71186 | -45.66516 | 2024-11-22 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9770bf64-1912-3dd9-ad84-56651a711150 | -13.1026 | -43.3236 | 2024-11-22 04:14:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 95243909-c03e-3140-a4dd-bb6c110f3cdb | -9.29696 | -43.12774 | 2024-11-22 04:14:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 570e6596-2569-3d83-8c29-89e8a66a691b | -12.42445 | -46.63373 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 484f98af-2509-393e-94a0-9ef9685db639 | -8.93377 | -44.25348 | 2024-11-22 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eb67572-ba2f-3f7e-924b-666cb8038287 | -12.44431 | -46.66522 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fced597-6bff-3db5-a7e4-a28ace300363 | -7.6509 | -44.50266 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7cb69f0-922f-30f8-bb3f-b3388b2b206f | -12.44084 | -46.6646 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7775271-3cda-3a2a-b307-90fcd16bb960 | -13.36866 | -43.9258 | 2024-11-22 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed4e3bfd-fa67-30ed-a1f7-237efddd7de8 | -9.30029 | -43.12826 | 2024-11-22 04:14:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e41c1226-f410-38ee-93ed-e6a8347a7ffd | -11.73732 | -47.24146 | 2024-11-22 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fccf3b41-0a45-323f-881c-39faf2aef5ab | -7.59448 | -45.26231 | 2024-11-22 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b8f77ff-acfc-3786-b3ff-feace60aeac0 | -11.51278 | -48.12857 | 2024-11-22 04:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dff8098-03b7-3b4f-a423-cc05582155ba | -8.72444 | -44.01413 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c6e36c3-40b2-37e7-a4c4-583e340721f3 | -8.931 | -44.24942 | 2024-11-22 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68155201-442e-3b54-abec-f97a7e16f3e4 | -12.34988 | -46.67314 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e987e6f-6ec9-36d8-834d-6be1aa61c0a6 | -11.3694 | -57.57876 | 2024-11-22 04:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a6c2b113-2057-368c-8205-1a8193c232be | -7.65427 | -44.5032 | 2024-11-22 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37405b15-0c4b-3b48-8b71-fd76463608f7 | -12.44148 | -46.66069 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8726e27-60cd-3ecd-b7be-cd8942c7fb8c | -7.7568 | -46.22384 | 2024-11-22 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 310d3537-008b-365a-8863-a740612219c8 | -14.13264 | -41.63067 | 2024-11-22 04:14:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48f0ba1d-c93f-3f3a-b235-b19635233900 | -12.86835 | -40.67826 | 2024-11-22 04:14:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 525d93da-6bf8-3648-8eb7-05d9d2c0f119 | -12.13905 | -40.89554 | 2024-11-22 04:14:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dab5688-b7d7-34a3-9aad-77860c380db7 | -11.73802 | -47.2373 | 2024-11-22 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5513c68-eae0-37df-a3c7-b5df99dfc4f8 | -9.35867 | -35.49305 | 2024-11-22 04:14:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b168b6c0-25d8-3f44-92c4-29b007d49053 | -8.72666 | -44.02169 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 992e526f-5d49-3574-a251-c6fefd80e172 | -11.94816 | -49.54244 | 2024-11-22 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eac38cdd-c9cc-3b62-9a4a-2ba347415bde | -11.98004 | -44.24024 | 2024-11-22 04:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb277b9c-6511-3d79-b5a2-29ab410da074 | -9.50047 | -43.18895 | 2024-11-22 04:14:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d0fb12b1-caf1-3c45-9efe-02c20f7e7738 | -13.10371 | -43.31632 | 2024-11-22 04:14:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 726ba277-9b5d-3280-8294-3b316ef3cc97 | -7.47221 | -47.18328 | 2024-11-22 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b78e81fa-c6cb-3f0d-8251-910c271c6d65 | -10.73339 | -49.53519 | 2024-11-22 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69bf2197-13ed-3b3f-8307-26c019438fc5 | -8.71501 | -44.00902 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a650963f-6c5d-3872-b58c-129693cc24ee | -9.0493 | -36.03944 | 2024-11-22 04:14:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97c243dd-4ba9-32fd-a97b-437d8725e833 | -9.16179 | -44.30103 | 2024-11-22 04:14:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bb99dba-d905-3918-9daa-fbdc90348768 | -8.72333 | -44.02116 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50678e4a-7c0b-3087-894c-4a3713f35a02 | -8.93044 | -44.25294 | 2024-11-22 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6eba722b-508c-339a-b446-b5dc5cfec230 | -13.10316 | -43.31997 | 2024-11-22 04:14:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3988b231-2052-38e2-bf43-f9e16561d300 | -12.44779 | -46.66583 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09af01ba-6e62-32e3-93b5-eccab02d3c25 | -12.42381 | -46.63762 | 2024-11-22 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3880798-dbdc-3a46-b9df-ee2ad244de3c | -13.88573 | -43.07501 | 2024-11-22 04:14:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e74e90d8-1af8-3842-a2f6-6f1f6a99e6f6 | -8.71169 | -44.00849 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f32c4f2-9b27-307e-8ccb-b20a65fdaf37 | -8.72388 | -44.01765 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad7b01b9-4b69-3e66-8381-038c0a325ed8 | -11.66028 | -49.7562 | 2024-11-22 04:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55130037-8dd6-3789-8312-b68aa7205a18 | -13.87155 | -42.91637 | 2024-11-22 04:14:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff4c5475-b106-3528-a2ea-7e9049047d82 | -9.15845 | -44.30048 | 2024-11-22 04:14:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84772b4b-ad7b-3324-b5e5-0c68395119b0 | -9.48367 | -37.77582 | 2024-11-22 04:14:00 | NPP-375D | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c37cc884-35d2-3887-9965-8e91acd5ecca | -13.87099 | -42.92014 | 2024-11-22 04:14:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 73138805-7765-33f9-a3ae-8fe3be5fb3ef | -9.35813 | -35.49348 | 2024-11-22 04:14:00 | NPP-375D | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| fe933e93-ad05-334c-8f43-590c7b6292b0 | -8.92766 | -44.24888 | 2024-11-22 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b031c628-2e47-3472-8c78-f13072b9d5b6 | -12.77713 | -49.30631 | 2024-11-22 04:14:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87c0beb4-903c-354e-8ce6-03e12c66fc9c | -8.72111 | -44.0136 | 2024-11-22 04:14:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f70d69ad-fcb7-3237-9689-c70dbbea2074 | -7.71598 | -45.66185 | 2024-11-22 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5639a23-dfa8-3387-bc3d-bf7190240f1d | -10.96841 | -37.17683 | 2024-11-22 04:14:00 | NPP-375D | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d9f33ee-761b-3796-bec5-388431597b4f | -8.93711 | -44.25402 | 2024-11-22 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9724836e-2efd-307e-8ec1-e97944757aa3 | -13.86813 | -42.91584 | 2024-11-22 04:14:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93bbb0ff-c321-3399-9db3-e348c10faba4 | -10.66163 | -48.10938 | 2024-11-22 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6287f8a-1b38-3d10-ab88-1d8542188688 | -10.65781 | -48.10868 | 2024-11-22 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a521302b-5851-3698-8cbd-81260d391ee9 | -10.85045 | -41.23965 | 2024-11-22 04:14:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
