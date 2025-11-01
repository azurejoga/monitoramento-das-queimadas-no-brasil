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
| 183b5f1a-c5dc-3d6b-a185-dded0936432c | -4.49761 | -49.86945 | 2025-11-01 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f67bf603-634c-3327-bd69-a39ad49832ce | -5.19044 | -44.90903 | 2025-11-01 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 272d0be7-307e-3ed8-9af1-a0d77927ff78 | -3.01832 | -53.96589 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 214494bc-57dc-3fee-a6a7-034507479629 | -7.34474 | -46.21367 | 2025-11-01 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af819b27-7e91-398a-8bd0-4e10ab7bc11d | -3.56993 | -50.26467 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09e663cc-185c-378a-bac5-f903be4da7db | -10.41068 | -44.33791 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 849bcd16-36ea-3547-8ff1-58129199f7cd | -4.49861 | -49.86868 | 2025-11-01 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b68c2394-01d9-39cb-8f82-3a75e84cf153 | -5.45623 | -45.40467 | 2025-11-01 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46107ec5-a852-399a-8b10-6c9e7c96e4b9 | -6.88594 | -42.8437 | 2025-11-01 05:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90776759-7256-3de2-9e63-45bf30023e8f | -10.41406 | -44.36536 | 2025-11-01 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4ea34b5c-4cc6-30c0-baa6-d7679a23f253 | -3.58391 | -50.26035 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 940f9cce-20ad-3bc1-99c0-06410bc99767 | -3.53114 | -53.00204 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7294d713-1980-3b96-a2c1-7e7cc5060927 | -4.7942 | -46.4721 | 2025-11-01 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7876daf-f828-3bb4-8cd4-ac9378296ff3 | -3.56938 | -50.26817 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0a78785-4a69-350a-817f-4fdde1e02421 | -5.3996 | -48.25069 | 2025-11-01 05:08:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61d57d58-91d4-3604-a459-d4c28751d335 | -6.56294 | -52.7957 | 2025-11-01 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18f63ffe-0323-3b69-9d88-b38b5d21031e | -3.59577 | -54.04027 | 2025-11-01 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92522cf6-cb77-3dbf-be99-950e20d700c3 | -4.84979 | -47.52707 | 2025-11-01 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e612188-c735-37f8-bd1e-004921e19eab | -3.4704 | -50.93927 | 2025-11-01 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3a8457-db5c-3eb1-8c50-73c502f54b22 | -3.46138 | -52.87117 | 2025-11-01 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b2b93fb-3f38-3466-8e0c-6235977b0285 | -6.46223 | -46.73053 | 2025-11-01 05:08:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37a7c470-7ee4-31f2-bbfb-8ebc3055c8c1 | -5.14342 | -49.87014 | 2025-11-01 05:08:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f865e213-cbee-3cba-a2ef-edac7e2a2518 | -4.67386 | -45.81105 | 2025-11-01 05:08:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a179196-f5a6-3c54-b9cc-5d43907f8546 | -4.43435 | -45.91372 | 2025-11-01 05:08:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbe7d8a4-de07-378b-a0a2-d3fdcd37dd5b | -10.63478 | -52.18876 | 2025-11-01 05:08:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f6b570e-239c-3a16-b0a2-2b099b604340 | -10.4231 | -49.37296 | 2025-11-01 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a63295a-0f03-366d-b5da-6960480ecad2 | -4.212 | -53.49393 | 2025-11-01 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29cf7579-d7f7-3a0e-afc3-838b3c621fdd | -5.48985 | -43.08568 | 2025-11-01 05:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c470b013-3a3e-37a4-9e4d-bdaf4df22fd8 | -10.4222 | -44.331 | 2025-11-01 05:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8a9aac53-ec9a-31b7-8732-5cbaa4b35bd2 | -10.4219 | -44.3542 | 2025-11-01 05:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 3ad28149-707c-36f3-af64-003316708677 | -3.234 | -50.5789 | 2025-11-01 05:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| be46c84d-7537-39b6-b1a6-fd95cfcde418 | -10.4028 | -44.3568 | 2025-11-01 05:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ca6c51ec-0d7f-3aff-8f7b-2bdf4ce596e1 | -12.64963 | -60.42829 | 2025-11-01 05:10:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb4f97bf-7e57-39a8-8b67-63da5833e47e | -15.02524 | -56.45951 | 2025-11-01 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94cd8e38-ca06-3790-a75d-d3e38f90127c | -11.79639 | -56.96067 | 2025-11-01 05:10:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfc82bac-4177-330f-a4f8-1151ccb7b52b | -12.88466 | -48.26876 | 2025-11-01 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38168e0d-b86a-3e11-ae2a-9570b192ac81 | -13.00409 | -55.972 | 2025-11-01 05:10:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccc7c9a6-3831-3c48-9682-79ce23251429 | -11.38739 | -48.93185 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b58f528-b604-3005-8d42-4a6f338b7166 | -11.37819 | -48.92498 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d5efb6e-5f76-35f6-ac35-f89375f34eab | -12.87512 | -54.74263 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f54f9954-38ed-3e00-8bfd-b7126bbf45d9 | -11.7381 | -59.31104 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eea66651-8fc4-36a1-9a5b-075d17bd62d8 | -12.02376 | -63.75027 | 2025-11-01 05:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fbc7778-d723-350c-b5dc-fa2be58dd0f1 | -12.59937 | -48.33964 | 2025-11-01 05:10:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae77f38c-180e-39ba-9b86-43a4cea0a5f3 | -15.55599 | -51.50132 | 2025-11-01 05:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b4ac02f-3ad1-387e-91d4-ff8d28010b9b | -12.02459 | -63.74576 | 2025-11-01 05:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f4ab2d7-5f86-3636-8296-2a32dd8ca51d | -12.88954 | -48.27277 | 2025-11-01 05:10:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 392718f1-26da-31bd-95c3-89b81ec81d1a | -11.33847 | -54.38033 | 2025-11-01 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b93cf72b-2fdb-3024-873f-acababa80e85 | -12.88802 | -54.7528 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a6ce34a-f58e-3138-8e7b-fd12b46aa0eb | -11.73938 | -59.30331 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aa05a06-2fac-35e7-9a10-4ddef2155368 | -11.73644 | -47.47182 | 2025-11-01 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f0a651f-b4ad-31c7-9208-996cb124c3fa | -16.24531 | -60.1689 | 2025-11-01 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29973d4e-27b2-3f11-b656-5f6f466a57c3 | -12.17123 | -53.62884 | 2025-11-01 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d17037e-49d2-308c-96e0-4a3a50e0f15f | -11.37793 | -48.92303 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c218179-ca06-3e54-9c08-366c0cc1e633 | -13.84519 | -47.0599 | 2025-11-01 05:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 227c91ba-8dc8-3860-87b0-ed72ebf305d1 | -12.3216 | -57.72363 | 2025-11-01 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39c96c2e-a120-3935-a189-a9d9770aedb9 | -11.97804 | -60.73568 | 2025-11-01 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e448cd1f-ad66-3027-a5f0-1d4c2748a48d | -16.23995 | -55.72852 | 2025-11-01 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 42f287d2-13e8-3292-890e-84bdf7ba33af | -11.37748 | -48.93057 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df7dcc15-d615-3e18-8372-8700741f4919 | -13.84521 | -47.06155 | 2025-11-01 05:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 783ec117-e599-38ed-91d5-d6d68a5845ee | -11.85497 | -58.81481 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5669c7e-97bb-3747-98ab-175a3c523cdc | -11.73689 | -47.4682 | 2025-11-01 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1cadb3e-37eb-3a24-9f41-226201e3c4db | -12.3177 | -57.72663 | 2025-11-01 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71e472e8-1fde-3b25-83dc-fd2d809527b6 | -12.08852 | -47.87706 | 2025-11-01 05:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6ce3e2a-2faa-3ad4-a2ee-8765236ffec0 | -11.97434 | -60.73501 | 2025-11-01 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 955fb01f-cbf2-33b2-919a-083e73e4c07e | -12.7633 | -61.45847 | 2025-11-01 05:10:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9b8eb8e-c4d4-389f-b86c-2c0be78998ce | -15.56094 | -51.49762 | 2025-11-01 05:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71fe9c4f-a784-3530-8e83-06209664f6f5 | -13.32155 | -60.71766 | 2025-11-01 05:10:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c35c3ae1-3b59-356a-9a7f-99c66ddb6a65 | -11.72832 | -59.30542 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e38dd235-42e7-3230-9cb8-510b86d37c93 | -11.37719 | -48.9286 | 2025-11-01 05:10:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88dc8df1-92bd-3380-9512-5085278689c0 | -11.97967 | -60.73448 | 2025-11-01 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc8d9f70-3f4c-3bb4-819a-53c2ac1f5bae | -9.23048 | -65.74628 | 2025-11-01 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a46cef8c-0290-3596-99d2-5ffc0ad5257a | -13.32956 | -60.71465 | 2025-11-01 05:10:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2283326b-0b83-3fd1-9418-507ddd0e8f0b | -13.72142 | -51.45477 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a27765f-813c-3b48-a32d-aebbaf565375 | -15.55709 | -51.49258 | 2025-11-01 05:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5efa8fb9-783c-31dc-8022-bae07ba15b2e | -13.32593 | -60.714 | 2025-11-01 05:10:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa85fcb8-1cbf-3f75-907d-ff27c4b067fe | -9.48594 | -64.49961 | 2025-11-01 05:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d53dee8-cf69-3d00-ba4e-6c97cc7fccc9 | -11.74221 | -59.30777 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c6305c6-7c3e-343d-bd6c-4b05ac12c8bc | -13.84477 | -47.06342 | 2025-11-01 05:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74fbbf8b-4481-3beb-988f-bc390d5daaff | -13.72291 | -51.46088 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75210d51-88ed-36c4-8ff9-965a74712ec0 | -12.31713 | -57.73019 | 2025-11-01 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0231f5f2-3aeb-36cf-ba74-84c1bcf90e72 | -13.20494 | -43.13157 | 2025-11-01 05:10:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24194e14-3831-311f-a8a4-385ee8f5b221 | -9.22513 | -65.74529 | 2025-11-01 05:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 65a937ee-d00d-3c8a-8a7f-2bcdf358c3ff | -12.17871 | -60.69467 | 2025-11-01 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad39c699-f4e6-31ef-a717-2dce20a729b1 | -11.74285 | -59.3039 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fda822e-c260-3a45-b0ac-db7dcb041603 | -12.88039 | -54.75568 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16da5b07-0e8c-3662-b73d-2c24af8c6220 | -12.88391 | -54.75623 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f14c504-2a7c-35fd-8e3d-d7115032d730 | -9.84947 | -61.98877 | 2025-11-01 05:10:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 142ab7f8-e87a-3075-b236-2f1efc623172 | -13.71711 | -51.45417 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 64c5f015-4457-39db-86ad-f91e1117c247 | -15.56039 | -51.50197 | 2025-11-01 05:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ba62f92-6012-3195-9d89-40feff207e5b | -11.20017 | -53.83606 | 2025-11-01 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c67a3d17-0028-3797-a1bc-da15ff116ddd | -12.88744 | -54.75677 | 2025-11-01 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e61a5c3-d803-371f-be43-90083035d181 | -13.72088 | -51.45893 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5213fed-b3c9-3f60-8b3f-c20ea7329294 | -13.71658 | -51.45833 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4a36654-20c4-397d-b47a-e527b35613fd | -11.72896 | -59.30155 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b29ded9d-f175-37e1-9f5b-c9d8c9825382 | -11.74632 | -59.3045 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb9e7fba-da22-3a06-bc79-e1ee9d3ce98c | -11.73096 | -47.47107 | 2025-11-01 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ed6d20-09fc-314c-80e9-c35f58062e79 | -12.65325 | -60.4289 | 2025-11-01 05:10:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a75d5cb2-e252-36e6-a56f-56bd8e9e6cf0 | -12.0254 | -63.7413 | 2025-11-01 05:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6ef3ab3-b8d9-32d0-97de-39428d606b79 | -13.72519 | -51.45955 | 2025-11-01 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11e635d0-b607-384f-8d35-9d9fdb8e232d | -11.73462 | -59.31045 | 2025-11-01 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README29.md)
