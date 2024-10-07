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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0f007e5-08b8-32dd-81b7-2e87c2dac7ad | -10.88785 | -63.9126 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d348fdd7-5ba0-3c5e-9cd6-8c10bf0ffab8 | -10.88749 | -63.90992 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eadf8dfa-cc53-353e-8b3a-b38c47440e27 | -10.88487 | -63.90707 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf0c4a9f-2943-3e1b-9677-648654f1bebf | -10.88406 | -63.91189 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e32447be-5474-322f-b1d9-d60bbefd473b | -10.88369 | -63.90931 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d62f17a6-f130-3a40-b0e9-7b12fd0f2c2c | -10.88183 | -63.90196 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72d70247-0328-354a-96cf-4495185b4f23 | -10.88105 | -63.90661 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a11844c-e195-32a6-81e7-4103f8d60c42 | -10.87957 | -63.8922 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c1b4bae-f13d-3a5b-885d-0774b5b9b1ce | -10.87949 | -63.91587 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 688f0fd7-390e-3386-8382-cf0d395c6d74 | -10.87877 | -63.89695 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8138ff4-2d9f-3525-9ae3-441ba2e62163 | -10.87871 | -63.92051 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 255a0a8b-776b-3573-80c2-46318ef6006f | -10.878 | -63.90155 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 026d9a7f-e656-3b09-88b9-52f99fd4dd6d | -10.87723 | -63.90612 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3f109a0-26a1-37a3-9a61-b86203537728 | -10.87647 | -63.91061 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ac43b2-26b7-30f3-b2a3-52e94005dfb3 | -10.87575 | -63.89169 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75941372-7c51-3c39-a2ab-c632115c8f53 | -10.8757 | -63.91518 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23decfbe-ab21-3b5e-b20a-9e523c17a9b8 | -10.87497 | -63.89637 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04f9f31e-6862-35c9-8906-25c61ac30bb4 | -10.87492 | -63.91985 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b173bb3-0670-3016-9648-caef71eed260 | -10.87419 | -63.90102 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f12c343b-f8fc-38a7-be8f-417d47a9acde | -10.87411 | -63.92467 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c51aeb40-e8d9-3b60-87f9-7b95f065920e | -10.87341 | -63.90559 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 115e864d-5f6e-329f-8cd6-7b83d7848552 | -10.87267 | -63.90998 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d8a4927-d836-3787-aa5f-a71bc5eb49d5 | -10.87194 | -63.89118 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eab4194d-ec4c-33d5-9e3e-097c0e48346e | -10.87117 | -63.89577 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b91dc401-307d-3330-992a-450e715239e1 | -10.87112 | -63.91919 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffabe4eb-06d8-34a0-98f2-bf34722dc809 | -10.87038 | -63.90046 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3b79a91-f46f-30c3-ac9f-7eee2ce536c7 | -10.87031 | -63.92403 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d5fa069-ea3d-3aab-84e4-2a27f856135b | -10.8696 | -63.90508 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43bd1061-edec-3ffe-8dd8-4327d3e4e07e | -10.86892 | -63.88596 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d33a5e1d-d229-31ee-8b70-961543cb9b1c | -10.86886 | -63.90946 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef6f7239-2898-3bef-ad15-47c8555afc65 | -10.86813 | -63.89064 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ec366ec-2add-35d6-aede-0d8a7e1e37a5 | -10.8681 | -63.91395 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e61fb88-422f-3cbe-b478-78cc398a04db | -10.86736 | -63.89524 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ef4c77-adb0-3633-b68c-c6bfdabe7602 | -10.86731 | -63.91865 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad11e8e-598b-3291-b453-2bab843d4bf6 | -10.86433 | -63.89008 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1316effe-ab78-3dc1-a19b-df5f6e4e49b3 | -10.86427 | -63.91351 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93059324-a3f6-308b-8cc7-3b0406759573 | -10.86354 | -63.89473 | 2024-10-07 05:18:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f7c2c70-673a-3e18-8fc3-7e1722add96d | -10.84457 | -64.17083 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| beb495e7-9a96-3a9e-9703-f48b400ba035 | -10.84249 | -64.16779 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 021351cb-a0ab-3033-9f21-14e512b458ba | -10.84166 | -64.17252 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8caf00f5-2c77-3b99-8234-d7d59ffcc88a | -10.84069 | -64.1703 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb24b1c0-fe68-3e32-94a7-a3419e4bb2e6 | -10.80915 | -65.18259 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb9c8f4c-4dda-3c40-a7f9-331803f6eddc | -10.80374 | -65.18925 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf6a4fa8-ec4e-3a18-a335-1b1a1fde2c5f | -10.79895 | -65.1924 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd898fa-8fec-39fc-937f-b3265d797cac | -11.66211 | -65.21061 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5410d1b9-47d4-3357-8c03-4ab7bca7b73d | -11.65806 | -65.20988 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91062282-f007-38e9-be67-509591bb5a8a | -11.58428 | -65.01586 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68cf4183-9ef3-32a7-89eb-beae30df4a49 | -11.57965 | -65.01866 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 131d8e2d-4c87-3332-8f20-965982b74343 | -11.54205 | -65.13635 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e140b3d0-9a63-3548-b585-b223ea65ad80 | -11.54194 | -65.13702 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b8a3eb7-9450-304b-8d52-dda10ff5f621 | -11.54143 | -65.14001 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 876a46c2-28d9-360a-9701-038026316d99 | -11.54129 | -65.14068 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30f4b43f-b1f6-3259-aef6-87fd1431f627 | -11.53739 | -65.13924 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91026e8b-bde1-35c0-a206-ca689467d525 | -11.53206 | -65.04949 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b451c8a4-cd89-3d6d-9d79-be048253d168 | -11.53144 | -65.05306 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76f12b2f-d4e1-3687-95f2-250e0a88efa6 | -11.5293 | -65.13774 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe8f91e8-a68c-3432-9d7c-781c20891a42 | -11.52867 | -65.14139 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4be067a4-c176-3c58-8676-edfbf9184e5e | -11.52803 | -65.04877 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d23c8769-4531-3263-b9f4-4fd4aab5b0a3 | -11.52742 | -65.05234 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3edb2c40-5078-3062-b513-d8b5d6fbf59b | -11.52464 | -65.1406 | 2024-10-07 05:18:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8d0f854-ad05-36c6-933b-fa30ac69f412 | -19.13711 | -57.51338 | 2024-10-07 05:21:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 416145e4-7ab5-3086-a7cf-24e6d76cf11e | -19.11585 | -57.5135 | 2024-10-07 05:21:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5f1b3b96-ce66-3783-9f28-e4d40a3dbf90 | -18.62929 | -57.26624 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 393177fd-e69d-3588-9e34-dcedfb4540d7 | -18.62812 | -57.26433 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3f1c639f-e7d4-3328-8f65-33ad2bd85d70 | -18.65123 | -57.24907 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| a728f438-893d-32a0-866f-53f196851efd | -18.65057 | -57.25408 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 0c911b75-ed48-38e7-95a6-bffdfae42aee | -18.64802 | -57.24349 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 683eb5f0-e237-311a-ac0b-8ac15d5b721d | -18.64736 | -57.2485 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| bf31bf45-4cf0-3026-afac-33794dadc4f1 | -18.6467 | -57.25351 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 279120d7-44bc-37a3-bfc1-fe9d4c00048f | -18.6435 | -57.24793 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4b23e2d2-3a99-3d06-9642-141517dbfc3f | -18.64284 | -57.25293 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cc7299c5-ddf7-396f-814f-5c892ed8ddb7 | -18.64218 | -57.25795 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d836914e-ae45-3311-ae0e-0daa6280e881 | -18.63832 | -57.25737 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fe12138a-912c-31af-89c5-0ee009c5248e | -18.63446 | -57.2568 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 801c9dac-de90-36d6-8a9a-daeb763b003c | -20.26023 | -56.52824 | 2024-10-07 05:21:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 62bf39c5-bcc6-32ca-ae5c-37c85c10a2b3 | -20.25659 | -56.52376 | 2024-10-07 05:21:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e1c0a312-9c43-3104-9b03-60909e0e55a6 | -20.21856 | -55.99551 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f72652dc-ec2d-3ed0-8115-0ae13de7ecf7 | -20.21805 | -55.99969 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c74c9504-b555-3bcb-a323-d9110523da57 | -19.66212 | -56.50805 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6cd9a3dd-d5ed-3bce-869f-eadc95aa7869 | -19.66163 | -56.51186 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 81b791d2-f2ae-3ac2-9600-afac3daf535d | -19.6598 | -56.461 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f10145a5-c484-3e0a-8880-0982ee4d7c2f | -19.65882 | -56.46867 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d24df64c-acf3-3d4a-b1c5-94fdf02792f2 | -17.85266 | -57.68035 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6b341ff0-d599-3543-a579-4148aa25fd75 | -17.84892 | -57.67978 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 61720c5b-4820-33dc-8ce7-52e4b6415684 | -17.84766 | -57.68903 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6a2b9ce5-8def-3565-a4e0-1f1378a3fa8d | -17.84703 | -57.69365 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 448899d5-8b86-36a1-9428-1b7ad52c5387 | -17.84519 | -57.67924 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e4d05a2f-77fa-3f27-9b9b-0998675fdae3 | -17.8433 | -57.69309 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6c50d51d-a268-3a38-8569-9cacf76bbf8e | -17.84083 | -57.68329 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 69299aba-315b-3b50-af67-e98c07618fc5 | -20.75727 | -49.47881 | 2024-10-07 05:21:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 127f2a93-dbc2-3b2f-90af-3b519b742658 | -18.89728 | -54.54748 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61c40e2f-94aa-3e11-b79c-14048901ebdc | -18.89678 | -54.55171 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6d644f0-ac6e-317b-9805-f4eb7f049290 | -18.89627 | -54.55611 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f57d988-7f0c-3c8a-be47-a796eb6c6f22 | -18.8957 | -54.56088 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1cc22a3c-9495-392f-8cc3-4f2ed320c331 | -18.90296 | -54.53896 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74d3c9ae-394e-3ae4-8388-4431be3da799 | -18.89897 | -54.5331 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1dd6c65-d8bf-3a9b-abfe-965ee89050a0 | -18.58912 | -47.30721 | 2024-10-07 05:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f3f16da-892d-3741-b96e-e84571886c4a | -21.56718 | -47.7613 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13b201eb-4c97-3ff1-97b0-13b7d828988e | -21.56291 | -47.71898 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9900b934-707f-322c-9e3d-8005f4eeeff6 | -21.56243 | -47.72592 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README126.md)
