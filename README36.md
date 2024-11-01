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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b79924cc-d292-3804-a215-d6f96166333f | -2.8891 | -49.49947 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32624db9-4ed0-31c0-a870-3aaef98579ad | -2.88849 | -49.41288 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c9bf2d6-7aa7-389c-bfb2-2744627d3c4b | -2.88788 | -49.41671 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fdf31d0-28e7-3e36-bd7e-edf05b45e985 | -2.88577 | -49.4753 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89964fd3-d1be-39db-9145-99ddc57ce72b | -2.88516 | -49.47915 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5914393-b869-3d0c-bea5-24e517ae454e | -2.87823 | -49.38779 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34d79580-5c67-3045-8644-9d02171f900e | -2.87416 | -49.39105 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b69054-50c7-3d32-94fc-3d98bc59bb63 | -2.85761 | -49.3611 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11f69630-3fe7-3daa-b6c9-d31bd86e890c | -2.85525 | -49.44291 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c93da21-f21b-3fab-8c51-479ab264a27b | -2.85465 | -49.44673 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61428c6b-1918-3237-b41b-d4feb2da63a9 | -2.85397 | -49.38394 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a49a61d3-8847-3742-bb8d-c78a532d372e | -2.85342 | -49.45443 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aeacd2a-b8b8-3521-b2ff-086c8169f35f | -2.85336 | -49.38776 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e07350-0926-3608-9776-1a8022ac4717 | -2.85275 | -49.3916 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92785663-f053-3d68-988d-39a4082a46da | -2.8522 | -49.46211 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0ae59e3-899f-3b90-9c6c-57eb2e97c8cf | -2.85117 | -49.44619 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cea974c6-b835-368e-91df-c936f71a7ae7 | -2.84933 | -49.45772 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9242718-1458-36a8-86c8-72647af49c34 | -2.84928 | -49.39105 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ace9c244-0e18-3ecf-b9fc-de17ee0b604d | -2.84193 | -49.37033 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45c62962-e30d-3045-9315-96e41d7730b2 | -2.84034 | -49.49177 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42483c1e-96af-36d4-ad15-5f2ed0459423 | -2.83847 | -49.36979 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6eb9c3f-bcb7-3f33-998f-c9976b3c0014 | -2.82278 | -49.31278 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 219bac5e-536f-3e9d-9e49-25bf0ab5009e | -2.82035 | -49.31271 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae975892-6b83-374e-a3c7-67d6fe112839 | -2.81976 | -49.3165 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d086fea-ed78-3d9c-874c-eeff7394efea | -2.81933 | -49.31224 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1f74356-d6db-3d16-a9af-5860bb3414aa | -2.81871 | -49.31603 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9c66a3d-7f8c-3511-9763-de98e3bce842 | -2.81749 | -49.30837 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a990c8c4-dca8-3f0d-8424-2a1abafb6d10 | -2.81689 | -49.31216 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e56574a-8f12-3a24-9a15-62ea8bbb0bce | -2.8163 | -49.31596 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fc83653-25f8-3589-a75a-b4c1e04d1a8d | -2.81511 | -49.32355 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b40e9b3-669d-387a-abcc-45ee8a4df6e6 | -2.81451 | -49.32735 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d731710-6f46-39fd-a76f-ad89314070d6 | -2.81403 | -49.30782 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f6f9fae-c4e3-3061-94cd-27d78ff072d1 | -2.81165 | -49.32299 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfa92c22-2185-3322-8289-bcbd490c2a71 | -2.81105 | -49.3268 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| babee59c-818f-3e8e-9162-374c4aa9a393 | -2.80819 | -49.32245 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37f8ec18-c198-300c-98b7-bd9a63c87793 | -2.80759 | -49.32625 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c976351-85f7-38b0-867e-e328fe1eef02 | -2.80413 | -49.3257 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f969ecdf-d230-337e-b75b-49bbf619093a | -2.79315 | -49.32785 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48c5495d-571a-311f-8777-2dc337a1ea56 | -2.79283 | -49.47636 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80927af0-b591-356f-b689-ab975f4794eb | -2.79255 | -49.33166 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb44db3c-d600-3228-b861-28bee5887509 | -2.79112 | -49.47651 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f6c9d78-be7f-395c-8b9a-3860dc5c2dad | -2.78909 | -49.3311 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eec02505-83e3-3e7a-8748-a68abea17b37 | -2.78849 | -49.33492 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e5fe27-a97b-3929-bd2e-1daf39445e83 | -2.78764 | -49.47595 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a57dac9-ca25-36de-9ed1-7be2088bfade | -2.78703 | -49.4798 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aedc2ba-eee6-3b5e-bfad-8b8e908012c6 | -2.78503 | -49.33437 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61fcf556-338e-3122-8898-16c0b5499c39 | -2.78355 | -49.47925 | 2024-11-01 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82272dac-754e-3190-998b-fdb0043f5f24 | -2.34422 | -49.10464 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61505ef1-41f3-36d4-8e85-c1cf21c4060e | -2.33898 | -49.11537 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d0ec13a-6a05-383c-96fa-a5eda17b59ec | -2.32135 | -48.94083 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eec59d4f-ece3-3891-82b5-a719e62fe6a9 | -2.21081 | -49.57644 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 366cb3ea-0ca9-3ba0-b56f-d3d83bd73295 | -2.20729 | -49.57588 | 2024-11-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72862eb0-8759-325e-8898-191063beecaf | -2.52736 | -49.18671 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0e298bf-66cd-3ab1-8614-4b64cbd1786f | -2.51825 | -49.09343 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6432f9c-015d-3b23-965b-083810b7178d | -2.49311 | -49.07413 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd73607-12c9-3196-9054-d0ca7d1b4c61 | -2.48967 | -49.07359 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db5cdbbe-1118-3341-94cd-9b420fd28bbc | -2.48908 | -49.07732 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddf08cba-cbc5-30a9-aedf-c30e51cd341e | -2.39961 | -49.17902 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12026be7-74ed-3cf9-94de-5fcd8306993e | -2.39735 | -49.17093 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56bea347-9674-3369-b9e2-3ff01fa576a5 | -2.39675 | -49.1747 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f1a45d6-ec38-38cb-b280-653caad90540 | -2.39104 | -49.16606 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 124ebe65-89cf-300e-848a-d3338795fae0 | -2.38758 | -49.16551 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 690b001d-442a-391f-bad4-96dd437fb46d | -2.38413 | -49.16497 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7be8c18-406c-3e4d-b6cd-3780ce8d1a3d | -2.34833 | -48.90285 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d372ea7-546d-3225-ae4e-77caf6ddaf72 | -2.34482 | -49.10088 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a34f086a-f144-3265-9021-d9ddff177524 | -2.34078 | -49.1041 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4738b091-55a2-3c5f-98df-4c7568a27d91 | -3.50807 | -50.47313 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c09d065c-6f89-3a56-ae37-f32808b3b167 | -3.50738 | -50.47731 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ae106fb-519e-336f-b049-48ab27117331 | -3.50682 | -50.47472 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22fd7959-daf0-34da-b96b-aea38d3cde0e | -3.46238 | -50.33513 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e79f0394-2376-3e94-af6e-a824df03f138 | -3.45985 | -50.30505 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf6c6e4f-3237-323d-8da3-ba5f09866e82 | -3.45919 | -50.30917 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9505d3f-232d-3b11-80a3-54a848872501 | -3.45626 | -50.30449 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30dfac10-3845-38aa-b137-9c694da068d0 | -3.45559 | -50.3086 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91a4b22d-0c42-398b-ba18-2edef6087efd | -3.43494 | -50.32228 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 415eaa69-7f24-36fb-b51e-360a2e5b93dc | -3.43135 | -50.32167 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 482862f7-152d-3463-b2e8-0e88ad743bc6 | -3.39688 | -50.34305 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 584f9f71-a13f-35c6-bc2b-8d8806082247 | -3.39393 | -50.33836 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaef47d9-a93d-3bc7-9008-b8fc0c9af653 | -3.39328 | -50.34247 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bb998d0-fb54-34a0-968e-f557271a7e6b | -3.38968 | -50.34189 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9f65059-639d-31d3-9d48-7ee6af0bd50b | -3.26645 | -50.34021 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1418dcac-e28a-361e-8320-b00abfe6c559 | -3.26579 | -50.34435 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7fcdb4d-4804-32ca-9112-d2062a46a83c | -3.25518 | -50.04496 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d13f666-bd25-38f0-85de-4bf37a697367 | -3.25453 | -50.04899 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3d774b7-3616-3f8a-adac-5916f006091e | -3.25163 | -50.04439 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f94ecf69-05ea-37ea-aea0-998a45ef06ad | -3.25097 | -50.04843 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b21afb9e-9ff2-3e8a-83e6-0acecd88aede | -3.25006 | -50.1897 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b817c05-9349-3686-9d2b-2592cd149683 | -3.24867 | -50.04506 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2566614-f895-3fce-ad75-f752008f5208 | -3.24804 | -50.04911 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8814b677-090a-325a-94c3-716dd09fc77f | -3.24742 | -50.04786 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9b4fd0dd-f3db-3122-b8c3-e19af4c19c3f | -3.24448 | -50.04853 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae3d623a-9040-327e-9792-b1184486c293 | -3.1829 | -50.58187 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dff2a280-e16c-3258-86e1-b186ed98e9f9 | -3.18221 | -50.58615 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854fc1c3-8930-3b68-ad01-3b8595a62597 | -3.18151 | -50.59043 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5848cf84-d4b7-3cf9-9502-80c10c8b241e | -3.17855 | -50.58556 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 133ebf1d-8d71-3e80-93f4-f249a2d37260 | -3.17785 | -50.58984 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dac8a1f7-5700-3d8c-95fc-e116c56b9c36 | -3.17559 | -50.58069 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b39949f8-a7ce-3190-9222-28de72363ce6 | -3.17489 | -50.58497 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4f1e331-3d21-3dcb-9956-7da9c179b758 | -3.1742 | -50.58925 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3063c34-2498-3bde-8ba0-cb4555758fa7 | -3.17193 | -50.5801 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README37.md)
