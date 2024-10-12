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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b65ab99-5102-311c-8567-061ae7165b2e | -12.94404 | -62.61827 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3a1ed55-a1fe-3150-b904-84f2c53b22b9 | -12.94338 | -62.51552 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb47b1c-3a73-3fee-b70f-1a0b2508e205 | -12.94223 | -62.52266 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7213ddcd-6055-3117-9b9b-1f6f8b911c5a | -12.9389 | -62.5221 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f3bde9c-14ce-37be-b73e-33d0874be0cc | -12.93348 | -62.7268 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 158040b7-7079-321b-a70f-1565f5b21897 | -12.93014 | -62.72625 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0454a60-4e11-3331-ba11-dad804302553 | -12.92956 | -62.72983 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| de092182-1315-310e-a53f-0cba286b376f | -12.92841 | -62.73701 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e235c64-81b8-3431-87e5-8e2fd3683198 | -12.92727 | -62.50917 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3acc0dc0-a50f-365c-9e92-31b96e6ccfbf | -12.9267 | -62.51274 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f064ebc6-a43c-3588-95c1-a0f2f7be8c3c | -12.92556 | -62.51988 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dbd662d-cbcb-33b1-a3dc-79b897ccab31 | -12.92506 | -62.73645 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cba2cb0-04f0-3c3c-a37a-b9c63dcc53e4 | -12.92448 | -62.74004 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7b19a71-7833-357e-bb4a-56638e7c756e | -12.92114 | -62.73949 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4033df6-0ff6-30cf-9be0-56b45f0e1369 | -12.91826 | -62.50792 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8c61444-8130-3014-a74b-41b185aa32c6 | -12.91722 | -62.74252 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 914aa2fa-b1cd-3a73-a731-1af40c4a978d | -12.91492 | -62.50736 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eef9e5c2-32d3-33e1-9c2b-28179e122169 | -12.91445 | -62.73837 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd8ab29d-4a96-3917-bdc6-761e96930db8 | -12.91436 | -62.51092 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7795c98-f18e-310c-97c8-5cebed020ed2 | -12.91151 | -62.52877 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e6b0f18-a32d-3a3c-80b9-0e2a4f945db6 | -12.90818 | -62.52822 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 094e4887-47a6-3275-9794-6f41e8c66429 | -12.90761 | -62.53178 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ace72a1a-78f7-309f-ba44-60b5bc0ba47a | -12.90427 | -62.53123 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a3b2a5-cd70-3324-b432-fc63168d9836 | -12.90371 | -62.5348 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3a29559-f9c7-39d6-95cd-ca069a93c2e2 | -12.90094 | -62.53067 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 011f00d5-edbb-3a23-832f-a8b7182de51f | -12.88786 | -62.79663 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9ac2860-a6fb-3679-9dcd-35c73e5dd6ff | -12.88451 | -62.79608 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfdb1760-232f-393c-9a71-e1136114a103 | -12.88393 | -62.79968 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2975d4f6-16b0-386c-9f93-fc117a41bf11 | -12.84622 | -62.80844 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8e41532-46d2-37e3-982f-fcf7dba4f447 | -12.84287 | -62.80788 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e6d94a2-758a-3af0-8af8-445eab484b01 | -12.84181 | -62.90024 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c2af857-87fd-3ccc-b48d-d46e3bca8228 | -12.84123 | -62.90385 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deed53dd-e3cf-3991-b8dc-fe4c9a4fa783 | -12.8373 | -62.90689 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a5518a4-1cc5-3a83-bd2e-e167b248800f | -12.83672 | -62.91051 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60b436c6-e166-3830-9dc9-fddcf68e6eb4 | -12.83336 | -62.90995 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3bddcb0-18c4-33be-9168-b2e9a3ac4b6f | -12.83 | -62.90939 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9763945-1070-3d43-a6c3-84d600b47414 | -12.82942 | -62.913 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f043683-b922-301c-bcf7-a3e53869ac23 | -12.82607 | -62.91244 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca9eeb2-0712-31e4-82e0-ae435c716fd9 | -12.82329 | -62.90826 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c57301e0-ca07-3417-bdb1-f90cecbeeeb5 | -12.82274 | -62.99742 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca04e144-9fb7-3277-b329-2e1647183207 | -12.81994 | -62.90771 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ec9cb6e-3309-3c4d-9276-9f137c05fd0f | -12.81938 | -62.99686 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a91d2562-f227-3dc9-9de0-2de85dc68aa8 | -12.81935 | -62.91132 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dde13ef-9f86-32dd-a32e-2c36b0e750d9 | -12.81543 | -62.99992 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25d6677c-64c5-3c2f-a00c-f22380c9f3bf | -12.81207 | -62.99935 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 973659cc-5062-3941-b90f-41cf421f894b | -12.77859 | -62.72753 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8263b5fe-2b65-3113-87f1-92478d71d4ec | -12.76862 | -63.03305 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5254f5f-5f35-3267-87b3-1cc00f58b2d4 | -12.76803 | -63.03668 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ade16fd-d617-397f-b5e8-c73a3ecfd555 | -13.0086 | -62.47146 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fedf2ee-e5a2-3118-b9f4-604cd5e191c2 | -13.0047 | -62.47446 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 714dd644-53f6-3b0d-8119-8fa434b67667 | -13.00323 | -62.73064 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1be0afff-79a9-3be5-9fa7-a541c3b04a25 | -13.00265 | -62.73423 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47805b3-818a-3dc0-a060-489f507029a6 | -13.00193 | -62.47035 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 202325aa-fa90-3b56-9848-49bf4cd2b76c | -13.00136 | -62.4739 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15ed1113-33a9-3a1b-a09d-116b3b2a041e | -12.99931 | -62.73366 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a031d23-fc4b-3cce-8470-b1e4143c278b | -12.99873 | -62.73725 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a794134-8085-3d0e-807c-57edcff3c9c5 | -12.99803 | -62.47335 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad11fcc9-e43e-34c0-b5d0-8ac2f7fb0292 | -12.99746 | -62.47691 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f0e3aed-dc81-38b8-b573-c83a2ad9e242 | -12.9969 | -62.48046 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7deef446-e146-3de3-a809-4e9c707bbc2f | -12.99597 | -62.7331 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2f5fcc3-0f09-37ae-841c-3deea167b9ff | -12.99539 | -62.73669 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be364109-9e31-397d-9bdc-9f135e1bce39 | -12.99483 | -62.72968 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ca01a98-d83d-3b90-910c-56b7fcdc9d6e | -12.99481 | -62.74028 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7dad993-4ce3-3119-ba4d-c80b404abfc1 | -12.99426 | -62.73327 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5439e06f-7bae-316a-87b1-289c1ec9f427 | -12.99413 | -62.47636 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c52b855-3d3e-37af-83ac-4e984d5da2df | -12.99368 | -62.73686 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 620a02af-7a5f-3a3b-a28a-c73b6b4333b6 | -12.99356 | -62.47991 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0b49b78-9511-38d3-8cb1-7135038ea5d6 | -12.99311 | -62.74045 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1451d1cd-3ee9-3f8d-8205-ca330b8fd395 | -12.993 | -62.48347 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaa77825-5cca-3d2b-a623-204cc90de780 | -12.99148 | -62.72913 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1742cd0-949e-34d9-8cb5-24f8397f08f0 | -12.99091 | -62.73271 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf8f16b0-7e6e-3871-a97f-174c672b3fbc | -12.99023 | -62.47936 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7d80dee-4606-33e0-ac0a-4afca2add148 | -12.98976 | -62.73989 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ef3c179-2e1c-3a74-bdf6-df32cab67636 | -12.98966 | -62.48292 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8c34e9a-2f53-337e-b972-3f28e7de8b31 | -12.98814 | -62.72857 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce9b0dcc-a64a-3e8a-b74c-a225cecad93e | -12.98804 | -62.75066 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a007b9ea-065a-3fb6-a45a-10e38823835c | -12.98757 | -62.73216 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a82a5bc-cb50-3e1e-8066-19ec2af2151f | -12.98747 | -62.75425 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ee6a852-555a-3794-aa7f-d0413b13c67c | -12.98699 | -62.73574 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c86ff175-107b-3cf2-9197-9e5d13ca383a | -12.98633 | -62.48237 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c52333a3-0d02-3ee6-85ec-e29dffadd5df | -12.9846 | -62.77221 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7ce2560-0285-304a-9da2-694e395f5ffd | -12.98355 | -62.75729 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e065818d-2c23-3458-a667-d313fe0d0db4 | -12.98299 | -62.48183 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e07d79e-e531-3d52-bc81-8e68ae36a18c | -12.98068 | -62.77525 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 766b54d5-71a3-3ab3-80bd-b446b9b755dd | -12.98057 | -62.79738 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3c763ed-fcfa-3d86-8bd1-972577198049 | -12.97966 | -62.48128 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d63552b-aac6-345c-909f-758247308faf | -12.97925 | -62.71972 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73bf3307-0471-342c-a42a-eb2079429745 | -12.97868 | -62.72331 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d546487d-6a12-3147-9c5a-5c7a0aa40d59 | -12.97725 | -62.66787 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6264e318-9555-305d-82b4-8379089cefe8 | -12.97723 | -62.79682 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8778ad3-2362-355a-98dc-105fd01b5a3d | -12.97675 | -62.77828 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b50a60e-cfe5-3eeb-bc4f-a4b8c82d2397 | -12.97665 | -62.80042 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d9aa304-0369-337c-a94b-1a4451af7f04 | -12.97591 | -62.71916 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37ea38fb-c1f9-3b08-8152-56e28d09669f | -12.97388 | -62.79626 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2e640b2-4318-3a1f-8c74-4df90d6375a0 | -12.97341 | -62.77773 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8e66e6e-469c-3df5-871f-6e18eb20f83e | -12.97334 | -62.6709 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd2cb760-4b5c-31cb-b75c-9d23a29cf7ae | -12.9733 | -62.79986 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e0e7e1d-2abe-3c72-aa77-253af0947a37 | -12.97283 | -62.78131 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9678e0e0-8c58-37c7-a0b0-f0da6eec632f | -12.97226 | -62.78492 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a17e91c-1e8a-39d8-85d1-68b76543f21f | -12.97168 | -62.78851 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README116.md)
