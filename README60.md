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
| 7f7bc100-708c-38b3-aa5b-7b330b7a3236 | -15.85514 | -44.89643 | 2025-10-30 04:27:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 338e31bc-705f-330c-85a5-86220e3785e6 | -13.27729 | -47.73933 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52960b02-3994-31f7-8cb7-789dc25742db | -12.88596 | -48.63821 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7bba116-8c31-32c9-82ac-087e0d794e5e | -12.60414 | -43.20106 | 2025-10-30 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a069c5df-a623-3552-b0fe-d06358712476 | -12.31979 | -50.31009 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa1f5e97-907c-39bd-b1aa-e7aefcf6e2fe | -13.52088 | -47.33316 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdce40a3-c4a2-3342-aafc-9143923bfe71 | -13.0762 | -48.21321 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fbc075ea-014f-3fa6-981c-031c9bdda7a8 | -13.79184 | -52.79495 | 2025-10-30 04:27:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68a62450-d13c-3e6e-a6e2-34c91b72b959 | -13.41358 | -43.74852 | 2025-10-30 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ee07430-a95b-3577-b675-9c568e5452a7 | -15.01692 | -46.30703 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3329c207-c748-3de3-9526-2cccf08d3280 | -13.48773 | -47.99802 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d274ea4-6245-3590-9ed2-5e95848090f3 | -13.95204 | -48.45303 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa90c3a1-f791-3126-8b1c-3271ae7fb597 | -14.33523 | -49.8517 | 2025-10-30 04:27:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b27e26d-fda4-3ed5-af58-79dab3685f0a | -11.95404 | -49.93845 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dce82f0f-f3d1-31a8-8453-1acfce65e8bf | -12.51281 | -50.56438 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ae06d7bf-419c-30f7-a1a2-7e4f5c898175 | -15.02089 | -46.32727 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dac07131-eed0-3160-8ad9-2df72d6cad0c | -13.95478 | -48.45716 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e10d4f46-a9d4-31ef-b7ea-42b007ddd191 | -13.56894 | -47.15486 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 396c29c1-19ad-383c-af1e-21a37c007201 | -12.3679 | -50.15304 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ff93fd32-e798-3029-b4ab-e962a3f575f4 | -13.29456 | -47.3689 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9847fbf7-9f21-39ec-9593-5da8aff69a6b | -15.62424 | -48.87657 | 2025-10-30 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3885f858-f97c-307e-a144-28ac57d730ad | -12.50995 | -50.55962 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 70278cf6-3565-359f-adf9-34f4b9a3bf5e | -13.03894 | -47.52628 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb27321-2395-3d2b-b95a-92ef668c0ef0 | -12.32527 | -48.06399 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 198bd0ac-437a-351a-bab7-28f77005a0f6 | -14.7791 | -44.99005 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e7ecb35-0360-3a65-9877-8993a0ebdf35 | -12.90987 | -43.19249 | 2025-10-30 04:27:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51fe8a59-c6d5-33d5-8c10-40902d85924b | -12.32531 | -50.17028 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c7589d1-5bd8-37ea-b60a-cc4806a36d92 | -16.68036 | -41.36404 | 2025-10-30 04:27:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cf879f39-7b5b-348e-9a1d-8565e98334e2 | -13.9331 | -48.48631 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ae54496-9a3b-318d-b639-1ff46a505d43 | -14.57268 | -41.14552 | 2025-10-30 04:27:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6522bfa7-8054-3cd3-9c4f-6106aa54fbb1 | -13.95923 | -48.45061 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bbcad76a-9d63-3210-881b-7108db1edb72 | -13.68786 | -47.69755 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3411e88b-9358-358d-a976-53dd53cdd02b | -13.55846 | -47.13557 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b425fecb-90f6-334f-b6f9-e155cf841979 | -13.93766 | -48.45784 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f15c1dd0-c34c-34e9-b05c-69b9dce296fd | -12.31808 | -48.06638 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01fe8105-cc81-31ff-84c0-9b011f20f81c | -13.68037 | -47.17997 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 749f37a1-d094-3dc7-970e-3c4570eb22db | -13.19835 | -44.48756 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 206fc14a-d0f2-3c99-b49e-cb5b5e9d859f | -15.98738 | -45.64587 | 2025-10-30 04:27:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2954665-111c-30a4-98d7-4b3c77db2ecd | -12.39811 | -46.82563 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5fafdd5-3bd9-3eef-b24f-a3f3bb88dc81 | -13.07288 | -48.21266 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89460375-710c-3da9-9e23-dec007779732 | -12.50925 | -50.56376 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a183543d-e8e6-355e-bfdb-c7534f3111e5 | -12.30195 | -50.26538 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fc795ea-116a-3fc9-8da2-bb9ca0815539 | -12.98272 | -47.9039 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 403da399-b70a-3ded-aa3e-dc07da0e87c5 | -12.53061 | -47.54105 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2119ccb3-6765-31a1-90ad-efd20e96141b | -12.87813 | -48.64439 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c1262f5-a911-3abf-8874-b709bc7f3937 | -12.23254 | -46.47043 | 2025-10-30 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5985269-b86e-35bf-b667-69b1faba6337 | -13.51812 | -47.32906 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 897135c7-a1f6-36e6-8645-717c10a01616 | -13.37405 | -47.38224 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98044c16-30a7-30d9-91cd-e2ec3ff4df95 | -13.42425 | -47.36481 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 981df6d2-ffba-3951-aa45-7dc4e880d5f8 | -13.05109 | -48.66615 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a3429c-b710-397b-94f0-9c32ae78f058 | -14.22944 | -44.31674 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b10ecf34-db2f-3ea3-9eda-016b85509b3d | -13.61357 | -47.58763 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae04c6b8-3725-3987-b420-109c9422f5e0 | -18.54819 | -41.58078 | 2025-10-30 04:27:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae32546a-5e77-3e96-8400-8fcdc7392f20 | -14.77312 | -44.98053 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e524b226-9e9f-3d77-b8e0-f8f464baf108 | -12.14324 | -48.0124 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00158583-cf03-36ea-984c-a31ec17bc069 | -12.49073 | -50.56476 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5fcffd1c-5b9b-3ce6-b4f5-254661301dc2 | -14.92933 | -42.23872 | 2025-10-30 04:27:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d918563-be08-3263-9a6a-a08ed5846dd1 | -14.12896 | -44.07171 | 2025-10-30 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c090227a-5afd-339a-ba1b-ba57e89cc4c2 | -18.35803 | -42.2519 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fbcf3dd7-c837-3e07-aaab-05b5e68b0927 | -14.28781 | -42.3396 | 2025-10-30 04:27:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 40207eb2-0cda-3040-9e95-2adfd72395dc | -13.70352 | -47.68584 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19534b78-7231-37ce-876a-0db6246dd610 | -13.91116 | -48.45336 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f8999fa-105c-3000-bcb9-f206a83e0ddd | -13.95545 | -48.43172 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0047e3de-3f77-3571-b181-5ef3fe903923 | -13.3286 | -47.6935 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c72c0fca-1f6a-36a2-bd43-1f5ecf523dd8 | -15.8594 | -44.89258 | 2025-10-30 04:27:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97b66f83-cc41-361e-a472-d221d5a6c8cc | -13.4916 | -47.99504 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd7cb402-fe74-361b-88c6-3e1b6907ce3a | -13.95214 | -48.43117 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8f3a0fc-9128-364d-a879-7e85932f9cae | -15.02544 | -46.32016 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f4b2ff8-fce0-3be7-8a5a-20eabedf078d | -13.33048 | -47.44389 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3ec0cf5-023b-3260-94ea-e345f96b9f42 | -13.30063 | -47.06815 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad7f8bb7-8417-32cf-a027-33ce9c234d6b | -14.68245 | -46.3678 | 2025-10-30 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02895800-36c4-3e11-af89-fc611925db42 | -12.88653 | -48.63464 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ced82f1-b25a-3c81-a693-d6bd89fad1e8 | -13.6086 | -47.59766 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c597299f-d5f9-371c-90ce-da924c9cfbe1 | -13.61212 | -48.41145 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce128712-d130-3b4c-9c6d-da8b42260118 | -13.94371 | -48.46255 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7da45291-6caf-388b-be81-f4d8dde416d6 | -13.2317 | -48.55648 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f633fd92-3408-3ea2-9258-bb832ffc3a7d | -14.22754 | -48.13121 | 2025-10-30 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6aca052-91d8-3e53-87c6-64b2da634510 | -12.30264 | -50.26134 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aa33ab9-86eb-3a33-9477-6fdfda35fc06 | -12.70795 | -46.29352 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 602c52d4-bf1b-349e-aa9f-9c708ee0bb3d | -13.04181 | -46.74557 | 2025-10-30 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd1a0133-4dd2-3186-ae08-77532bd965d5 | -13.269 | -47.74884 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43a228ce-6f0c-3c58-9f12-80da97de89ac | -15.02828 | -46.32446 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d0ba665-cd65-386b-8da6-1c1dffe57cb2 | -13.95535 | -48.45361 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b186e8f7-f946-318d-b1d3-94c79ee30a54 | -14.69107 | -43.15259 | 2025-10-30 04:27:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e591fb43-c615-3e9c-9ed1-1769b8f75744 | -13.31501 | -47.47775 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1e61bce-b724-3838-9c0e-ebc159e4d420 | -13.3266 | -47.46872 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b58e5e78-2d85-33f7-8155-d86325c6de2a | -21.03819 | -45.68443 | 2025-10-30 04:29:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c92b98eb-4e31-3098-818f-57799ed0f2c4 | -20.53304 | -45.76739 | 2025-10-30 04:29:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 69d769cb-5797-3a29-955a-dd60d04aeeb5 | -20.7848 | -47.21043 | 2025-10-30 04:29:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea8a678f-8639-34fd-8f70-b8384597e7cf | -21.44593 | -43.40356 | 2025-10-30 04:29:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7455a2c2-d90a-3bca-aa02-b526edeca62b | -21.03881 | -45.67973 | 2025-10-30 04:29:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a16182c7-e043-3fbb-bac9-69783f22d78b | -4.2732 | -43.6908 | 2025-10-30 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6596f63f-d926-39c3-ad72-57e9551657de | -4.2649 | -59.6558 | 2025-10-30 04:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 53d5a97b-112e-311b-affe-d74cd202e277 | -12.4759 | -50.5707 | 2025-10-30 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8e3cec64-b5cc-3198-91d3-dcdcf5aedd97 | -13.3935 | -54.3138 | 2025-10-30 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b7532c65-13f1-3dd4-880c-7fde11fecc4d | -13.3743 | -54.3159 | 2025-10-30 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 34ae84a9-a1cf-32db-bbdb-a93888f66afe | -12.495 | -50.5684 | 2025-10-30 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| df895aa9-509f-379b-acd2-115a8fa4016b | -4.8411 | -42.7229 | 2025-10-30 04:30:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| de2b653f-293f-3ed5-8ba5-14aca04a3c4a | -4.2731 | -43.7139 | 2025-10-30 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 222ea0a7-39d4-38c4-bfad-8147d92053ca | -13.3746 | -54.2952 | 2025-10-30 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README61.md)
