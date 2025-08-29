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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd216c83-c22e-390d-87e1-2fa3f5bbba2f | -13.63047 | -48.25508 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f96f452b-e9df-34f5-97f5-3cfaf42937f8 | -9.11965 | -65.77714 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c91cfa9-848c-3f44-bbb8-6972dec3edb3 | -11.45603 | -47.30775 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aebedf8-c22e-31dd-a194-40e50efc63b9 | -13.41148 | -46.97546 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18e05612-a1e6-35b2-8bd5-e7ce7b2b4e12 | -14.34295 | -53.33232 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e62c3db-8d55-3b61-be60-cca6310894bc | -13.36847 | -51.75741 | 2025-08-29 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a92625b5-91b5-3f1e-86aa-426b428ab556 | -11.16344 | -47.15192 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c638274e-236c-3f15-909b-d1675bbf29b2 | -13.01979 | -56.91256 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b7171b9-86e6-3fb3-8d31-701b88b078de | -10.36585 | -57.82153 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d67caecb-156b-3495-8a95-7f47a6b2a20d | -9.78188 | -64.25352 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7a3fbb47-5709-3c20-b682-de873dcfc687 | -10.47597 | -57.96542 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90340695-227b-3aa2-8ff1-949ade624017 | -13.09821 | -57.12529 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5fd90cb-2b90-37db-b88b-929c94fbe8cf | -13.67058 | -46.87829 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48243261-7844-3030-98f0-b4b8ff73dc96 | -9.45428 | -60.57336 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cd23eedc-bfc5-392c-b237-e05e1c4d0dd4 | -11.37801 | -63.2597 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91ce65e6-37e6-3666-9ec8-48709e41141f | -12.70331 | -48.15159 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8f64cdf-fc04-355d-8094-c2c22f2b5bb8 | -9.1773 | -65.79898 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be75e04-4ef9-3dac-835c-168f76c724fc | -9.79732 | -67.84593 | 2025-08-29 05:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2d8f4e-1790-3898-a624-216e9fb85456 | -12.83335 | -48.17197 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 41790a1d-7778-3305-bfa4-f40f544ee2da | -13.03144 | -56.88169 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ae9aa5e-7a1f-3987-a566-adc3225b3090 | -14.33812 | -53.28255 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45dff03a-5ef8-3ea6-a163-e0b62e0d3ed8 | -12.91043 | -48.10788 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e97218-d3a7-359f-a660-8d52b59580b6 | -13.1899 | -45.28125 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48a47bd6-4ce7-30cf-91b3-e63226b14b58 | -7.56054 | -63.8436 | 2025-08-29 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62f58e51-dd0d-32fa-9ed8-e10602ddc1a1 | -12.87447 | -48.13832 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e4b6eb5-94ea-3bc2-a12d-e75c9e99134c | -10.98904 | -46.85842 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5e9a181-5a99-347b-8834-c3b261af0d33 | -9.77221 | -64.25169 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1fe0c02-2959-3b67-a6fc-efe9f627687d | -10.86256 | -60.81353 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fddbfca-8261-3386-9b6b-bbf96cd54c07 | -9.09265 | -65.7371 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e01fded7-a04e-3c7b-b280-123e981248fa | -10.07339 | -62.89111 | 2025-08-29 05:08:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a1c20fa-aa99-3caf-be29-67e47760c24c | -9.13741 | -65.80218 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7dc55a8-5102-3440-8d3e-e9fcf5290ff8 | -10.78694 | -56.2971 | 2025-08-29 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99e0b4a0-6bb5-3f13-9c9c-a9a5e5422756 | -9.80587 | -61.19653 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f79968e7-36e0-371c-872a-7cadfbbf0fe4 | -13.53657 | -46.86779 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4d481d0-103f-300d-88ab-8ea0ef986685 | -13.53519 | -46.87687 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8bde4cf-4307-3398-b9e3-4e51aaa0843f | -13.52682 | -46.94862 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e61168-1b36-3356-a5ea-7e21e848baac | -13.53942 | -46.94271 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec39f345-5fe9-3e16-a7b4-7f3adaa237a3 | -10.5943 | -54.90338 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d16cd028-b096-373b-862d-6c281fd8598b | -9.16235 | -65.7888 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 233e32df-5eac-3fcf-8669-effe805c0632 | -9.46433 | -60.56049 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5abc5e52-ff7d-3eae-b4c4-505ff32390a7 | -9.13677 | -65.80565 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af7522b9-eee6-39e4-8ff8-5916ee1842f7 | -12.82254 | -48.17281 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31f36d7e-348c-3f94-a45d-b43d87dc62c0 | -9.90916 | -62.14051 | 2025-08-29 05:08:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c785e7b-605b-3c09-bb3b-fb342ccaade1 | -10.36596 | -57.79932 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bd58fb9-b108-366b-a22e-b6cc88c2689d | -10.46082 | -57.94847 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16bac4fe-d9a3-3760-bd43-9499d007321b | -10.47934 | -57.96604 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f7ced4d-eca1-322d-929b-82f7926b860d | -11.94485 | -46.70673 | 2025-08-29 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab0b717e-6fb9-33de-a2a5-405311a00603 | -12.83989 | -48.15833 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26baaad5-e44d-3c24-8748-ac0bcef4fd5f | -11.59192 | -46.37488 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89ae3bb7-3a9e-3446-b75b-f4e0888b06cf | -12.91779 | -48.13519 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a0c8d93-9755-3e1e-a23a-74ece0eb82d1 | -12.91327 | -48.12836 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00423a62-3a99-3c75-be70-09090beaf90d | -9.11527 | -65.76667 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16c06991-a853-3641-8ccf-a936954c7bbd | -10.47676 | -57.93935 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31290d7c-b6ec-3808-b78e-c3c4ff947123 | -11.15355 | -54.30495 | 2025-08-29 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e725571f-0c5d-3db1-936f-e9b636b6bf46 | -9.80897 | -61.20229 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee365fa0-2a19-3e18-9cd6-f3d60ecf8e78 | -14.79164 | -59.71294 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d984e6fe-da5b-3b55-b413-d8806639e063 | -14.90222 | -46.4528 | 2025-08-29 05:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0503f7ad-f22e-37b4-973a-c86d381313fe | -9.78769 | -64.24903 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56aedf76-adb9-3754-84d0-4e3ce0871367 | -12.83334 | -48.16837 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e337acca-f028-30df-8d56-78bee7de17ea | -10.97476 | -46.92492 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 31ac6289-4e45-32ca-8541-8a0e9ff56a3e | -12.88547 | -48.13607 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3300b19-3aed-3b89-9d40-59c2539f6b30 | -13.40484 | -46.99434 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25917e7c-aa5e-3999-8fd9-09526f1c80d0 | -10.45745 | -57.9479 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24f48bf4-ef40-3583-a59b-15c2a84ef006 | -13.9746 | -46.32668 | 2025-08-29 05:08:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d0d1555-a607-3c4b-a90a-b90d44cf6276 | -9.11694 | -65.7885 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad338571-239a-3f2b-a50b-d62caa21a05c | -10.36422 | -57.81013 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2efaecf0-756b-38c2-9a76-1a7ed72489f5 | -8.2501 | -61.49703 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9dbfdb31-1a18-37da-a328-310d40eb7119 | -10.36364 | -57.81375 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f90e414c-27ec-3e23-bc18-509792491045 | -9.45207 | -60.56312 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b1d002b6-ab44-3aa3-980b-4f320c101a52 | -13.67852 | -46.9113 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0113174d-6a59-3371-9f65-9b5f194120a0 | -12.66619 | -60.26266 | 2025-08-29 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1bc4bf9-d313-33e4-84bc-2b9037aa6190 | -9.94166 | -46.35311 | 2025-08-29 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31f32d25-f767-3d11-8bf8-d2691982aa46 | -15.67348 | -52.75469 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bcae075-3743-3687-bdb8-6f0dbe1f5316 | -10.98218 | -46.89388 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3481aea7-5010-372c-bdf8-6a9b32a9ce46 | -8.1798 | -61.36277 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 641768c2-7151-3511-b27a-f5bf160fb541 | -13.63531 | -48.25952 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b01e165e-a419-3833-9443-cbe17700c903 | -10.32533 | -59.18143 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa5926c8-7847-3695-82af-8d3963477e34 | -8.13611 | -61.20925 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bba782b-effd-31b0-b796-85d277313668 | -8.95379 | -65.96737 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e55aa35e-499f-3db1-8215-3812231f2634 | -11.7062 | -60.1955 | 2025-08-29 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9865ae11-039b-30eb-8175-35b0f960b0e6 | -12.70857 | -48.15231 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed3ee5b4-8148-3d55-872b-b91e041e2804 | -10.4642 | -57.94902 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2f40f6-c11a-341f-8919-b1f0f60aebe2 | -9.60153 | -55.37375 | 2025-08-29 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a880d1c-45f3-38ca-8899-199210ed1908 | -10.93512 | -63.63522 | 2025-08-29 05:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb3865f0-d747-3afc-95dd-c42cca36ba8b | -12.68678 | -48.15551 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b544b13c-c3ec-3a07-998e-3eba614cd19a | -10.97863 | -46.89495 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f269e197-cf69-385f-a336-a29b56f82f68 | -13.01102 | -56.91151 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d03d8a7-10dc-3860-9711-2bb2010eed42 | -9.13003 | -65.29314 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1b49d60-824d-3c84-a880-c4fe4a5b259c | -13.45548 | -46.95927 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6c63bde-a0dd-362b-bdcf-53fdcb01d1b6 | -7.56742 | -63.8618 | 2025-08-29 05:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb487180-c1d2-381e-8ac1-03052ab99ac1 | -9.1528 | -65.7798 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 341146a4-ecf9-3c02-a476-532823eb35d0 | -10.07781 | -62.8918 | 2025-08-29 05:08:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 090dd8b1-b21f-35c3-b804-70712076cbb8 | -9.77124 | -64.25706 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a7d183a5-466d-3bf2-8aba-92c4ab91efee | -9.91347 | -54.72498 | 2025-08-29 05:08:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92e9e4f0-2f69-3a87-b17a-02dd27ed6b7e | -9.13588 | -65.29084 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a807e467-3651-3427-8dec-1a60bf13891b | -9.24694 | -59.78309 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76b08712-c743-356e-8a3d-6d9846dd4186 | -13.18869 | -45.29166 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f5ab443d-eb9a-3bc3-8f78-86a36b6b1a9e | -9.41437 | -60.57617 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 113de041-5586-3276-8e28-fa7126705588 | -11.40659 | -46.9126 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 118ee348-368f-331d-b719-31ac0de4f8f5 | -13.56031 | -46.91363 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README74.md)
