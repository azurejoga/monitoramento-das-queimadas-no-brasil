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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3924554-5fe0-3ba0-8267-47c592303eb5 | -2.83625 | -52.97563 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9cd6a86-5cfa-311c-95ae-f3bee4b78ba3 | -2.83566 | -52.97914 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4a316b-c43a-30d9-a769-5803b441212a | -2.68451 | -53.34525 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 052fb38c-e29b-3bdc-9973-7d2a237bd6ae | -2.68391 | -53.34889 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef74c4e1-874c-3c64-9bea-feeaeecba151 | -2.6833 | -53.35253 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72d09218-12e4-3807-ba1d-745e7bf05bb7 | -2.68017 | -53.33709 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1890f03-81e8-35a3-85b4-8ec9cd13a9a6 | -2.67957 | -53.34071 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 45cd3de8-780d-3c40-aacc-bbded926fd92 | -2.67897 | -53.34433 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ee4babe7-eabd-312d-bc50-6a3daaa0bcd7 | -2.67836 | -53.34797 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| e1dfce45-82ad-3f9a-9163-37ed0574d825 | -2.67775 | -53.3516 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 0265cc41-a610-3733-ae57-fb9bd61a0deb | -2.67714 | -53.35524 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cbd48a28-ec3f-351f-9a8c-9b86d6de7a6e | -2.67463 | -53.33616 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47185e8-71db-32c3-83a3-f3dc6b1e6c3d | -2.67402 | -53.3398 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bdbda0af-886e-3c4e-9ea3-a9fc68142aff | -2.67342 | -53.34342 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9e0b2617-5cc5-3b32-a1e1-0c9f9ada8fdc | -2.67281 | -53.34705 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 4df88353-0ab2-349f-b0fd-bc880fc7a5ed | -2.6722 | -53.35069 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| f0add281-da8f-301f-879b-ade4a24373b2 | -2.67159 | -53.35433 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f4d3cbab-7727-37ae-957e-f2e6c6ac0417 | -2.66848 | -53.33887 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4ec1ca68-a381-3a6d-8c8a-d9126d6a0e98 | -2.66787 | -53.34249 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62354491-36b6-37f7-b361-d577d0784869 | -2.66726 | -53.34612 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c9aced51-9113-3597-ad6a-64d928caeb62 | -2.66665 | -53.34975 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| a91bbc85-9489-34ac-b238-2545fe921c77 | -2.66605 | -53.35339 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 041e83e8-b981-3a56-ad5e-a14a69ed48ad | -2.66543 | -53.35704 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5646edbb-f8aa-3763-af35-925f6b940438 | -2.66233 | -53.34156 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 32662157-7aad-3a15-bf10-ca104bfce51b | -2.66172 | -53.34519 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 15e99a4f-97f5-32b7-8e45-0b304026f476 | -2.66111 | -53.34882 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 3b375287-1dba-38d5-8631-2644ebbcbfc0 | -2.6605 | -53.35244 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| fbf8817a-5ec9-3537-b411-10bfde27aeb4 | -2.65988 | -53.35609 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1d8747d8-dc65-3606-81cf-b3373bff948a | -2.65926 | -53.35978 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cd72c226-d341-3f54-b014-f86c0949158a | -2.65495 | -53.35151 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 40a2ddf1-e03c-3bf1-9445-ceef73e9cabe | -2.65434 | -53.35515 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 552f69c3-7c01-3aca-9c64-61d002f6b341 | -2.25236 | -53.47443 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97a7ba3e-852e-3742-9997-dffe5243b9bb | -2.25177 | -53.47806 | 2024-10-10 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09f144e6-9289-3547-a1e8-4f3bbb6532ee | -3.5114 | -53.01355 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1479b2f-f848-3fc5-907c-fa22e5fb6f50 | -3.51081 | -53.01711 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fb02f7b-0ee5-3c0a-aa96-77abe3729ed3 | -3.48247 | -53.28792 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16fdd5f3-9e22-3812-908a-b16dd4be3f39 | -3.47702 | -53.28693 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f18ff118-5ed4-3052-8173-36aebda1166e | -3.44884 | -52.81258 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c9864e5-f323-3aeb-a2af-34abf9786f09 | -3.44828 | -52.81596 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41fdc322-f0fc-32f6-936c-ab53d2172ef0 | -3.33623 | -53.22223 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 061b6e4c-adb0-3a0a-b3d9-917ec4b28278 | -3.33563 | -53.22572 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb1ca4b4-3e54-3c93-a024-34c5893f45ce | -3.33136 | -53.21787 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52301a9a-9d26-3de6-b068-2dcaf7d95b0b | -3.33077 | -53.22139 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60ad59d8-4440-3659-b30c-e14bb94fed42 | -3.33019 | -53.22483 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cd63fdea-7245-35fe-9a16-b6b00cb2bbfc | -3.32531 | -53.22057 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02477998-44c3-390a-9bd9-cd4f3cfa6723 | -3.23152 | -53.2729 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f83aee68-4c33-3275-a816-80ddaaef85f6 | -3.23095 | -53.27629 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a45e4a-e928-3262-8a03-2840621519f3 | -3.23038 | -53.27971 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8139f08a-4a2e-3bed-befa-112ee7bff620 | -3.88184 | -53.63136 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7700f99-3187-3f76-b517-25f6cc5a5443 | -3.88122 | -53.63506 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 078f303d-a194-3aae-b67b-fee9749b3f98 | -3.88088 | -53.63044 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75305dfa-6c7b-3495-aef1-44543c36339a | -3.88024 | -53.63415 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88ae19a9-88e5-3469-b178-366c254e7209 | -3.80462 | -52.41399 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 038fde78-93fa-3ef5-a296-a05ec548918e | -3.80411 | -52.41704 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b09895f-acd5-3fb5-876c-87d9ce9b9df2 | -3.8036 | -52.42008 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fdd06e6-03e0-37cd-8405-80326f97c583 | -3.73568 | -52.31143 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f73dfd5-35b9-365d-b487-d95f09c93dcb | -3.73519 | -52.31435 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00e89db9-f173-31b2-ae03-350eb0c1c2c0 | -4.25233 | -53.63737 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da245b1e-505b-3702-a3b5-984db0d8dd53 | -4.24681 | -53.63646 | 2024-10-10 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 791d312e-9fc9-3f76-babb-c900180f195f | -1.7444 | -54.24451 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1700339-3fbe-3e8f-9193-cf5c5993986c | -1.7426 | -54.24258 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 632ba7a9-8e26-3bd3-8e34-965a40ac9530 | -1.74118 | -54.25142 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41505737-31e5-3b66-b9f1-23de3cf5d3a2 | -1.7377 | -54.24786 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eafbd48-041d-3589-ba12-802d554ab341 | -1.74366 | -54.24889 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b9a3d0-d495-306e-8b6d-db8d1212e913 | -1.74188 | -54.24705 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2bfce17-ebac-3626-af47-baf05cbb0dc1 | -1.73844 | -54.24345 | 2024-10-10 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee71b3de-bc5b-3f93-a7d3-a8e8df058bcb | -3.56128 | -54.34396 | 2024-10-10 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3146313-4143-3242-83b6-4d13ae8b5145 | -3.56057 | -54.34808 | 2024-10-10 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40936be6-105b-300e-9836-c9123a6254b7 | -3.26307 | -54.18307 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c142ee87-e827-3501-8837-87715e7fd0ab | -3.26243 | -54.18698 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1962107c-7f19-3f23-8c55-e199ecf19b85 | -3.26242 | -54.18124 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca9b2274-e3e2-3bca-ad21-ab30e5944c97 | -3.26176 | -54.18513 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67b64381-b8e4-351f-befc-731c9b90f497 | -3.26117 | -54.19469 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7150a9dd-2f01-31fe-94b4-95b252dd2d99 | -3.26043 | -54.19284 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bd4dd9c-30b4-3a06-a11e-eac018683b80 | -3.25977 | -54.19673 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b139d96-7919-30e6-af9f-f1722e64c75e | -3.2573 | -54.18187 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97ab6254-e178-3632-84ba-069799b92d84 | -3.25668 | -54.18567 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7080ab0-ad0c-3f90-bb13-80a3a85a2084 | -3.25665 | -54.1801 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57e9f767-1fd4-373e-9f13-4513b229b18e | -3.25604 | -54.18954 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7f376533-c8ce-3eea-ac7c-f52891fe4176 | -3.256 | -54.18388 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28d2495e-1135-3823-a883-74898077b2d5 | -3.25538 | -54.19355 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 148dfa54-a9cd-30c3-a2ea-d0cb8940264c | -3.25534 | -54.18768 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 277860e8-1f11-3f0c-bc17-bc38c549fe1d | -3.25466 | -54.19166 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c074a4a-de73-3570-935d-61b861789026 | -3.25397 | -54.19568 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a43966d-7f81-36ce-96c8-ae30c9798e10 | -3.1307 | -53.73437 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e026f222-998f-3196-b0e8-03d9d6572ba6 | -3.13005 | -53.73818 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f4d6814-08cc-3514-b1fe-3dd57934a489 | -3.12441 | -53.7372 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e415e16f-d3b5-3f5b-9a38-fe2936d226b4 | -3.12375 | -53.74103 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffeca00e-2449-3e93-af11-3f2c4c6efc4a | -3.1223 | -53.73815 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f9abcef-455b-3af2-9779-6b7b09f4fbb0 | -3.12168 | -53.74199 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 629fbd73-780c-3987-9804-c0d33514b937 | -3.11941 | -53.73243 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36ec6be-1e0a-3b88-b0a0-8391ebf60b14 | -3.02031 | -53.8604 | 2024-10-10 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a84380e9-7a51-3bce-b273-2d91d4ed31ad | -2.97754 | -53.72032 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a942d6f5-9dd6-3f93-9511-530b44b2aabd | -2.95117 | -53.70403 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e929de2-0354-3e66-a568-bb2ceb612209 | -2.94552 | -53.70306 | 2024-10-10 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cba968a0-465e-3bec-ab9c-2f152f1bb5b8 | -2.88943 | -54.49061 | 2024-10-10 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a578d968-9f8d-3996-b688-376c80e380c8 | -2.8869 | -54.48943 | 2024-10-10 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c74a1067-678e-3081-856c-a8153a5b993f | -2.88623 | -54.49358 | 2024-10-10 04:17:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1a601d7-3432-351c-b007-41295f05bf39 | -1.76053 | -54.97493 | 2024-10-10 04:17:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c93b33c-ebfe-3e2e-8899-269e92cd57c4 | -1.61835 | -54.9188 | 2024-10-10 04:17:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
