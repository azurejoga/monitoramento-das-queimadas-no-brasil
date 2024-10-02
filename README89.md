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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ad8728-4f01-3771-919e-6114ab814dc4 | -11.27937 | -48.42208 | 2024-10-02 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85408876-055f-3d05-b625-6fc98110e24e | -11.27835 | -48.4195 | 2024-10-02 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edee2d8c-c344-32e0-b336-ba12f2c64bb3 | -4.49089 | -48.12022 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4fdea864-386a-34ad-9792-bb37ed9f92d0 | -4.48916 | -48.10807 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd7fd978-6645-37cd-b96c-e26e47d005e1 | -4.48902 | -48.12037 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b9049eb-0d27-3ed1-bbd2-3c1d584e97af | -4.48858 | -48.11195 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fbcc09f-d477-3472-9a91-96ec2d7a22da | -4.47161 | -48.11768 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a7aaf52-e6f8-3320-99bb-56dd92f94034 | -4.46873 | -48.11329 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc2d4015-d245-3ffe-840a-9d441362fbf3 | -4.46813 | -48.11715 | 2024-10-02 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1c3ddeb-b098-3a36-8982-f24dc92b77e8 | -4.72529 | -48.83926 | 2024-10-02 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e55abc3-49f0-3164-b452-fba48d74ad19 | -6.42016 | -48.27031 | 2024-10-02 04:46:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43987596-e428-3c48-a2cd-def55f4ba853 | -6.0949 | -49.33317 | 2024-10-02 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd5de0c6-8291-3886-be1d-e0dff4d2a2e9 | -6.09208 | -49.32903 | 2024-10-02 04:46:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c382873b-f7fa-309a-a179-bb78cdbf0d91 | -5.22156 | -47.95693 | 2024-10-02 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1a5e0a8-5733-3a1d-a375-f59dfe62549e | -5.22095 | -47.96092 | 2024-10-02 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ba9f0b3-25ac-3f7b-b111-dfe32169fa2c | -7.73549 | -49.89404 | 2024-10-02 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1fd4cdd-afa3-36ef-8db8-ccfc6deefe05 | -9.35024 | -49.4209 | 2024-10-02 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e00eb0-3777-3b1d-82ad-2f5c0868b8b2 | -8.89423 | -49.63106 | 2024-10-02 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 058497a2-5fec-3175-8b1e-2cc77a2e782d | -8.89367 | -49.63479 | 2024-10-02 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4344017e-dbf9-3f21-899c-219fa7de663b | -8.8931 | -49.63852 | 2024-10-02 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f8e1698-a09c-3ec2-802d-47b29270ca8f | -8.62262 | -49.47966 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9783f1a3-20b0-36b1-96a7-6dc4513cad2f | -8.6192 | -49.47914 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 956158cb-16a7-3582-a149-4e1a3ca2232a | -8.26315 | -49.35305 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b7f8b7f-4bbb-3200-8b17-263ca30e408c | -8.23844 | -49.76664 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c500310-3fa8-3b11-8c00-ba3f983f5221 | -8.23788 | -49.7703 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4c1c7d0-12f9-3e72-8cdf-373e593161a2 | -8.23505 | -49.76612 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff42b692-046a-3ed6-be70-a78eca3b74ab | -7.9806 | -49.46032 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c73b4cbe-7f87-3daa-8fa7-8992a5c368a6 | -9.78758 | -50.0765 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13dd4455-0b49-3f0f-aa19-40a4288122f6 | -9.73498 | -50.44454 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cc571d8-58a7-317b-a725-f560f3d41cd1 | -9.63012 | -50.10144 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c6057ba-4d6e-38ca-a768-7f8177f4e3bc | -9.62673 | -50.10091 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74b38f4d-f999-34f5-9d77-d988f3e5eeb3 | -9.62618 | -50.10458 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f9114a2-cf4d-3277-8cad-54da186751dd | -9.62225 | -50.10772 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 295ed2a0-1aa2-3398-acc9-5da802b1d518 | -9.62072 | -50.10808 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b3f17cc-f3e9-3a28-8d64-08671d9ca8c9 | -9.60211 | -50.09394 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51420ed7-f482-3b2d-81d5-b160d00607c4 | -9.60155 | -50.0976 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6384ad4-dbec-34cf-910c-2bf0d116a766 | -9.59873 | -50.09342 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c85077fd-ad6a-3fa9-b5f4-1516e72e17e2 | -9.59817 | -50.09708 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7a03f58-662b-3e02-9859-b012bc86b3df | -9.59769 | -50.19051 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 46a5bb17-cad4-3004-abf1-0134b35a0128 | -9.59713 | -50.19415 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae113a79-f8c6-3cd1-a5d8-02f26e2d6e73 | -9.59376 | -50.19362 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b97c7b97-0555-3ebb-befb-c00df2ced381 | -9.5932 | -50.19726 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c291d30-3160-3988-855b-85fb838fd4d5 | -9.59308 | -50.08504 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb91fe5c-cbd7-3209-a145-9599093c22cd | -9.59253 | -50.0887 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82d5d236-a73e-3dfa-898a-4984f40130ae | -9.59082 | -50.07718 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9f4fd4a-2628-35e7-96b5-b16121a9ec94 | -9.59038 | -50.1931 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 83c3dbe7-2c8d-320e-b7b7-6b10098f79d9 | -9.59026 | -50.08084 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac5e991f-7182-36f4-b92e-42d7fb3937a6 | -9.58982 | -50.19674 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef8a17af-6d05-3db7-99bb-a7b16fa4cd30 | -9.58927 | -50.20038 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da6327c2-2e40-351b-86b5-dd3d1b7234e4 | -9.58871 | -50.20402 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abd6878d-5a07-3ba8-800b-1daac14a0a8e | -9.58701 | -50.19258 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b702098-ea8b-3abb-a15c-51d8cebc5b9b | -9.58645 | -50.19622 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7fad1c01-cd4b-3751-b82b-1bad974e0500 | -9.58534 | -50.2035 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a011126-cc0c-378f-818e-0e1f3c0e4abc | -9.58364 | -50.19205 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2be66252-a001-3010-8a6c-522f95490d31 | -9.58082 | -50.1879 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5af49b96-2222-3ddf-b22f-3d3ff0a580ed | -9.58029 | -50.21388 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76e31680-9de4-3583-b356-3fa01f54ceaf | -9.57791 | -50.11642 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b328930-a95e-3093-af93-3867cdfe35c5 | -9.57636 | -50.217 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7de88347-7929-3ea7-8300-32c4aa55bd67 | -9.57581 | -50.22063 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47f019c0-c9a2-317e-86bb-ae9b393c394c | -9.57453 | -50.1159 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab1e712-047f-35d8-9358-c8cf827297bc | -9.57407 | -50.18684 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9375ffe-3d9c-3b92-94bb-3ed395fa19f0 | -9.57397 | -50.11956 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22568316-d5d4-3240-aa8d-9d44f046fe42 | -9.57341 | -50.12323 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dc1c221-2902-30a2-ab46-5a86ccc2c036 | -9.57299 | -50.21647 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d35eb81-9a8e-3496-85ca-f5c03fd7ae33 | -9.57244 | -50.22011 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6e91e86-fffb-3ae8-bfdd-09e293aa4a64 | -9.57014 | -50.18996 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ef9bcf2-8629-32e7-9de7-c4c2166c819a | -9.56907 | -50.21958 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63421c8-4d1a-3fe1-adf7-3b5e20420517 | -9.56788 | -50.18215 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 1d917146-a79f-3b27-ad9e-5a29cae215aa | -9.56506 | -50.17798 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f0baca82-fc50-3605-994b-03437d742715 | -9.56451 | -50.18163 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 6bb57ff1-6d07-3489-9db7-2c0bce280244 | -9.55614 | -50.21385 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99283a4c-92b1-390a-87ab-71c015cd819e | -9.54603 | -50.21228 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 690cd772-e740-3c9e-99b3-627206bbc848 | -9.54266 | -50.21175 | 2024-10-02 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe951c40-9f1a-3f22-b505-23c4fa1eb070 | -10.6275 | -49.90166 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6424c59-dfa3-3bb7-acfb-48982cc203ff | -10.62407 | -49.90114 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 299cb12d-7afe-386f-b468-2973109efc7a | -10.51436 | -49.79127 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3313a99b-7a3d-33b4-8789-eb2026e59ba0 | -10.51379 | -49.79509 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fab5b261-fc2f-31bc-aadb-9fa7b66bbda6 | -10.51149 | -49.78693 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cf7d6a0-b42f-3d61-b684-94c80371673f | -10.05169 | -50.30387 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14329c97-f0ee-388a-b14d-42cf064a1c18 | -10.03984 | -50.29082 | 2024-10-02 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96cc88cd-8d36-3479-8c80-9823bf23cf59 | -11.35137 | -50.79052 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fad1e2c4-a33e-360f-941f-7f3c5bf3bff9 | -11.35081 | -50.79414 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcba43c2-2a87-390c-99f5-5a5f06f1ba06 | -11.24981 | -50.02897 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecb7760a-8cc1-365b-97b4-144d13ca37ec | -11.24924 | -50.03276 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c389c4b-1857-3cea-9861-a72feb0e5351 | -11.15103 | -49.72736 | 2024-10-02 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 354318ea-b0f8-3890-96a7-a1eb647ae11f | -11.14698 | -49.73071 | 2024-10-02 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e4b6339-35b6-3f8f-b089-ee74c82f1d39 | -11.12427 | -49.59533 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4289e92-2fbc-3c24-a445-75f7592c0dc6 | -11.12193 | -49.58692 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ecbfe2d-cc85-3bc6-b9eb-b06adaf4b0a9 | -11.12136 | -49.59086 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61e2dbf8-d136-3dec-93f9-8dcc36ad2fda | -11.11557 | -49.60606 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c485660d-ffd8-3f86-a916-420c6241d504 | -11.11495 | -49.58585 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4ef80ab-1db3-3eb0-8bbb-41cbf0d69ba7 | -11.11442 | -49.61389 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 543aef4f-d387-3a26-aac9-8ef6ea28b361 | -11.11336 | -49.58681 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2832a1f-be56-33fc-93a5-b9f92bee75d1 | -11.11265 | -49.6016 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40f163a3-ff62-30f0-92c7-8ae241c202aa | -11.11208 | -49.60553 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 353495a6-5a67-3238-a141-5f7d62e9d6fd | -11.11151 | -49.60944 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cff8940d-98dd-3ac2-bcac-4bb50c1e9d07 | -11.1104 | -49.60645 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 906c2dd5-d956-3310-b75c-168a30f47915 | -11.10981 | -49.61037 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46c038a7-2c14-3b15-a49f-503a25661a68 | -11.1081 | -49.59807 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a57a174e-dd3a-3776-81c9-7d10287c69c4 | -11.10802 | -49.60891 | 2024-10-02 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README90.md)
