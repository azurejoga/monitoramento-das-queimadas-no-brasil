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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21c8920c-e3e6-305f-a4e3-668fad7b9568 | -4.33219 | -49.75674 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| aa03b158-a888-3575-9b3b-99704352b85f | -5.18161 | -55.99909 | 2025-11-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55a2b039-008c-3d49-a3bd-2e2eff0b78ad | -3.45551 | -49.97502 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 408bf9d8-0370-31a0-84ec-ae7d550d40e7 | -9.76 | -66.87335 | 2025-11-09 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cb09c04-d8fd-3897-904d-8713e1b4d568 | -2.60678 | -49.22199 | 2025-11-09 05:29:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 582e3b3f-b58f-3db2-9afa-129e0ac768e3 | -3.92243 | -51.01446 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94ca95f9-8667-3242-9800-f13b4c8cf429 | -2.71025 | -49.54507 | 2025-11-09 05:29:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb097449-2f46-3dd9-b499-540400464696 | -6.62576 | -55.01703 | 2025-11-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca14e936-15ed-326b-832a-a5ff6a45eef4 | -2.71562 | -60.01377 | 2025-11-09 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3914699a-aeef-3158-8eca-8813c222cde3 | -6.12855 | -52.64359 | 2025-11-09 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507b4605-6037-3f30-a7aa-82f56a173762 | -3.30944 | -50.16155 | 2025-11-09 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ff963f9-ee91-3ce2-99ae-d91565b70a2b | -4.39939 | -49.66719 | 2025-11-09 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 221bea54-2077-342c-bf6f-97e00d458061 | -3.9825 | -45.4389 | 2025-11-09 05:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 245b89b4-b0de-3f62-b845-42a97096256f | -3.9824 | -45.4614 | 2025-11-09 05:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 213.1 |
| 836e677a-989d-3466-ad28-95cae1fde63a | -10.3248 | -49.6341 | 2025-11-09 05:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c5c0a87a-44a2-3b43-979d-8c02dae117a1 | -3.9822 | -45.4838 | 2025-11-09 05:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b7f85318-6c77-3e98-870d-b1e1e723f0d7 | -4.4534 | -44.6447 | 2025-11-09 05:30:00 | GOES-19 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 39afceae-a5e7-3191-ab0b-3d30d7a06e95 | -4.001 | -45.4604 | 2025-11-09 05:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f113814f-b7a8-3441-bd85-c77cc9cd6ee7 | -10.3437 | -49.6321 | 2025-11-09 05:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 5e7aab2f-d5dd-32a2-a33b-66d55e6ff02c | -19.71494 | -58.11072 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b57fcf00-b0a0-3ac9-a6c9-eef310513a74 | -19.72843 | -58.11256 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 49e2a9c0-74a6-358c-bc83-8e20900302ec | -19.77002 | -58.10857 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| de012e06-1f3e-35f6-b471-8591460a3dc9 | -19.79541 | -58.04907 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bf667ee1-c4eb-35b4-9f92-3ac3bcc745a9 | -19.76326 | -58.08836 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 15565f16-c4fb-3c6c-81fe-da9cb160031c | -19.74137 | -58.11913 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| f025e3ab-563d-35e8-b3cb-fae5530a6613 | -19.74468 | -58.09066 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4f0b2de8-460d-3c66-b76c-849d113ebd3d | -19.75708 | -58.102 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 12b8b0a9-f45b-30aa-9982-f48adfea9fda | -20.25562 | -58.14919 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b68581d-8737-3404-bc82-9744740543cb | -19.75652 | -58.10674 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dfaffb35-e082-3676-93fb-a990cf46713a | -19.74586 | -58.11974 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| fd08b304-7d3d-3c35-a7e1-d56b23fba16f | -19.73008 | -58.09834 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d5043e3b-02d2-351c-b131-b6fd81d15da8 | -19.74531 | -58.12447 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| db963844-9da4-3839-b26c-a7997e88fd5a | -19.73852 | -58.1043 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 49d203ee-9533-346b-8347-f3ebf23af5d0 | -19.76552 | -58.10796 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3371f4ee-b539-38c5-a8f8-29704231e23e | -19.74919 | -58.09127 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| c5cc9372-491a-381b-ad84-7e9d8f4d60e0 | -19.77452 | -58.10918 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 92b53509-051b-3f38-9c99-8b5eb84898ea | -20.25507 | -58.15397 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 192cadec-079e-348e-a926-41d2ffe4c360 | -19.75927 | -58.04419 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 584f598c-10e7-3786-abcc-0513314d2e30 | -19.76046 | -58.11209 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 083954d7-3dc0-3b2d-a03f-cb51a8754ca9 | -19.71998 | -58.10659 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0e57f964-3439-3734-9721-c5a37a5f50b3 | -19.75819 | -58.0925 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4b1de3dc-e2aa-3252-aca5-0f4d642bb3be | -19.75875 | -58.08774 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 45395a01-3c96-342a-9058-9526230dcf61 | -19.72448 | -58.1072 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8c9787e9-9923-39f6-b81a-37db98bf1c59 | -19.79089 | -58.04846 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bbb0c276-6518-38c7-a816-30f8019dff40 | -19.73512 | -58.0942 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fbfad0a9-9aee-3a15-95ad-21699bfbbe05 | -19.7683 | -58.04541 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cc6e5e45-3bf6-354f-b658-f8948f6bd767 | -7.61192 | -60.91998 | 2025-11-09 05:31:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 791abf6c-3749-371e-a82a-73ca559c753f | -19.76158 | -58.10261 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e96cfeda-4035-3a79-bd7b-6780c70d5f23 | -7.61137 | -60.92355 | 2025-11-09 05:31:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1af774-a0a7-342c-a01d-9a4c5eb53d6f | -19.77282 | -58.04602 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 36111c8c-533f-3ea2-900b-00a3fb5a8097 | -19.73458 | -58.09895 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| beac8512-7bee-3d53-9d4c-953b417eb57f | -19.75935 | -58.12156 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4caf9c35-c58d-3ac1-822c-5fba11c5baf9 | -8.53192 | -63.49494 | 2025-11-09 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9b628be-fbd8-30d9-98a4-4d66f6dcfaba | -19.75597 | -58.11148 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 96678dc3-3594-3882-916d-a46521b8fbde | -19.72898 | -58.10782 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e0c00014-3f7c-3f52-9378-54d7b6056808 | -19.77734 | -58.04663 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b8e9a831-ec94-39f6-ad9a-4a7c9591c8cf | -19.7689 | -58.11805 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4347ac14-48b0-3bb6-aec5-1a12db96405a | -19.75091 | -58.11561 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 4cc6bf61-1d12-34f7-bcc4-9e6fec46686f | -19.80387 | -58.05507 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 52d1c686-6edf-370a-9ec8-1257d779f1e7 | -8.39029 | -63.3812 | 2025-11-09 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd9312e7-c212-3cfe-9046-d0732b5b0876 | -19.76378 | -58.04479 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dc36d935-c77e-3bce-bb0d-5d848c94248d | -19.7672 | -58.09372 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cb37a7f1-91b0-3250-b701-57c87a6c5362 | -19.72393 | -58.11195 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fe7f0ea7-15f4-381d-8d94-689275f20a36 | -19.74413 | -58.09542 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 153ca52b-b949-3a15-81e4-1b5141dde69c | -19.75369 | -58.09188 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| ee99b7ab-7639-3d97-b01f-3eca4b80370a | -19.72953 | -58.10308 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| dfc7a7c7-4242-3d1b-a045-85e47196cf48 | -19.7627 | -58.09311 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1700a911-5d47-3d50-87f4-18cfb98cd655 | -19.78637 | -58.04785 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c6808120-f6f6-31b6-8e60-90fe7254660a | -20.25959 | -58.1546 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1dc20f84-4dec-3cbc-be23-a9585977544f | -19.76496 | -58.1127 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4874a277-c807-3387-a2a8-700bbdb918ba | -19.73963 | -58.09481 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5d3e774b-154e-3048-b7a9-82a4ee6cabe9 | -19.80839 | -58.05567 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8f37a683-fe58-384d-ba37-3a21cbd71fd1 | -19.73347 | -58.10844 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1929148f-3617-3745-8a8b-207b77f86ef3 | -19.74302 | -58.10492 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c15657b7-ce02-3ae7-9c08-02f8ee61f10e | -20.25617 | -58.14439 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fdee5897-c87f-36f7-9756-591146e97b16 | -19.75541 | -58.11621 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 73920332-6803-3896-9642-a35fefa319bc | -19.76384 | -58.12217 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8568bdcb-7a47-37a0-9653-97c76adb992b | -19.78185 | -58.04724 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2d8e1eb0-4cc7-3f8f-b5c3-fe0e5b8859a2 | -19.71549 | -58.10598 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1cb8a876-a112-3c12-a47a-5722d758f584 | -19.75036 | -58.12035 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| f41714e4-6018-341d-9228-0794b09e8b71 | -19.72503 | -58.10247 | 2025-11-09 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 91939172-f908-362e-a6cd-50f259d80ed9 | -10.3437 | -49.6321 | 2025-11-09 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| eb9e0964-8887-3362-8506-327dc4632577 | -10.3248 | -49.6341 | 2025-11-09 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 00219b4b-2e41-31b9-b6ca-b1e06e34bcca | -2.96172 | -41.57139 | 2025-11-09 05:44:00 | AQUA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6108846f-2880-384a-84a8-2cc0a6fb57ba | -3.33466 | -44.3566 | 2025-11-09 05:44:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e9831ab4-38f3-3f85-bf6f-895881f4c381 | -3.98846 | -45.46257 | 2025-11-09 05:44:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 418.6 |
| a0c41132-2fa8-38c5-b0aa-f1967705963a | -4.83941 | -42.84365 | 2025-11-09 05:44:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| cba42599-aa94-34d1-bbe7-9769004e174e | -3.5882 | -41.65257 | 2025-11-09 05:44:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d3d1fa39-7e48-3e9d-826e-52175a86b485 | -3.44563 | -45.64454 | 2025-11-09 05:44:00 | AQUA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1a473729-6987-367f-9dfa-b0f1a2f12835 | -3.33155 | -44.37719 | 2025-11-09 05:44:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| fba70175-4744-30aa-8266-2e73943cb902 | -4.64188 | -46.39775 | 2025-11-09 05:44:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 76561aa1-9920-332b-b73a-9e0034b09b74 | -3.33311 | -44.36688 | 2025-11-09 05:44:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 5b60762f-c776-33f2-8110-cf8b303273c8 | -3.99026 | -45.45081 | 2025-11-09 05:44:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 497.4 |
| 7ad75c73-98dd-39dd-adef-d2d413c3a9fc | -2.91845 | -40.00454 | 2025-11-09 05:44:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 28.7 |
| a1e06d68-4d0d-3e43-911f-5f8c5142059a | -5.28705 | -44.94709 | 2025-11-09 05:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0c7251bd-28eb-3106-a2c0-4710e39bc27c | -3.45593 | -45.64608 | 2025-11-09 05:44:00 | AQUA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4b60683b-42e8-3c05-9afb-3b6633eee559 | -4.45332 | -44.64743 | 2025-11-09 05:44:00 | AQUA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f863a880-3e69-3615-8381-cd9e0cec6087 | -3.97838 | -45.46106 | 2025-11-09 05:44:00 | AQUA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dee44b2e-d853-3a14-b68f-445d55301dcd | -4.04706 | -46.42873 | 2025-11-09 05:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c002e8fa-2112-32dd-b97a-7746860b1e2f | -2.94158 | -49.36113 | 2025-11-09 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |


[Clique aqui para ver as próximas entradas](README36.md)
