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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20eb5d0a-aea2-3498-8d7a-6e70006479b2 | -8.2071 | -44.2032 | 2025-10-10 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 6c7fa3c3-99ef-3292-8270-26363871f538 | -9.1028 | -45.0248 | 2025-10-10 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| d4d3ab20-5375-3ccc-a6e3-a9846ec6cd4e | -7.5466 | -44.2933 | 2025-10-10 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 56cda227-ee85-3353-83aa-a2797f925478 | -9.4371 | -45.4656 | 2025-10-10 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 2f68616a-b778-3ef1-9955-a23fd2fa806d | -8.5007 | -46.3342 | 2025-10-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 444d508b-2726-3631-8fbf-cac596b68feb | -12.5082 | -47.481 | 2025-10-10 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ff3a7aae-6a74-3003-8e68-d52228c69e03 | -12.5733 | -48.1393 | 2025-10-10 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 77e18f66-c4cb-3445-bb7a-cbe39b498a26 | -10.1517 | -44.5984 | 2025-10-10 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 788409de-25d9-32ef-951c-87a484b7f1d9 | -8.5032 | -46.1321 | 2025-10-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.5 |
| f0e541dd-34e3-3c49-912e-5c09a6758b9e | -13.3295 | -47.7417 | 2025-10-10 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 52819fe3-2fdf-30af-9fe1-3d600d3e39fd | -8.5027 | -46.177 | 2025-10-10 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5626ca7d-6dff-309e-b324-032343666d80 | -8.6109 | -45.0792 | 2025-10-10 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 2da0193f-d40c-36d6-87c5-e43e9bbf3cbf | -14.2749 | -45.8879 | 2025-10-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| fcd92db7-2318-35cd-a523-d175a9e3fbb0 | -11.6451 | -44.2966 | 2025-10-10 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 3c011a5f-632e-32a3-b75b-82a747d1d514 | -8.1804 | -43.3445 | 2025-10-10 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| 7163bf50-b9c0-306d-bb79-3daa976fbfda | -16.7312 | -43.9931 | 2025-10-10 14:20:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 30a36fcd-4a82-3a71-8254-9616ec196c03 | -13.2864 | -47.9934 | 2025-10-10 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 8d66ba10-7599-3294-b48c-ce9111907d1b | -13.8496 | -45.8223 | 2025-10-10 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 77698ef3-da78-3a30-8291-88a1169fbc7d | -7.8687 | -44.1227 | 2025-10-10 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 874fe82b-ad4a-3c50-a752-f4bc352a50bf | -11.6446 | -44.32 | 2025-10-10 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 6f0f0e4b-c689-373a-9e55-83957c0dce47 | -13.004 | -51.0195 | 2025-10-10 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5e94f22b-2316-3642-bdd8-399fc09a54c3 | -12.9848 | -51.0219 | 2025-10-10 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d1cd9588-347b-35d0-aafb-21f2f2ebdb05 | -14.8884 | -47.2226 | 2025-10-10 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f5500ce6-d588-314b-afe3-b5af270340f9 | -15.3938 | -47.2938 | 2025-10-10 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 129.6 |
| fc259b1c-5e0d-34a6-9706-6c47d2de6f06 | -13.2667 | -48.0186 | 2025-10-10 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5838d813-1def-379c-bdd4-b32e85cb8f84 | -8.1804 | -43.3445 | 2025-10-10 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 161.7 |
| 66e6b535-d695-3db4-ad00-3e0c47440707 | -8.2077 | -44.1568 | 2025-10-10 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c23bba81-8052-30ec-b50a-357f26ad14d6 | -8.0151 | -44.4769 | 2025-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 1e6f6ecf-e052-3de7-8b0c-ec135e188674 | -15.3933 | -47.3166 | 2025-10-10 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| eb377ed6-cab4-3f52-9383-58ba01a4ccc3 | -13.3295 | -47.7417 | 2025-10-10 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 974e4f7d-dcc0-36ea-a04f-37ce83766e06 | -7.3149 | -44.8201 | 2025-10-10 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7f45e5f4-b1a2-3f2e-b609-07263ab696b8 | -11.7767 | -47.7587 | 2025-10-10 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 0b32ba08-ac42-3cfc-a711-c68b280d1d06 | -8.5027 | -46.177 | 2025-10-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1c20056c-3c0a-35a8-a611-a1e482c3db6c | -13.3488 | -47.7388 | 2025-10-10 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8938384d-677d-376f-96b1-d727daf699eb | -7.8687 | -44.1227 | 2025-10-10 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e60f1f8a-0897-3bec-947d-ff0f65323fb3 | -13.2859 | -48.0157 | 2025-10-10 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7ce1e30b-2675-3de4-a17c-e3a6eaace9df | -11.7585 | -43.3374 | 2025-10-10 14:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d3c4428f-8ee2-39ef-b7b9-c797f4981506 | -10.1898 | -44.5934 | 2025-10-10 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 0e4dc5fb-61ba-3f99-bb6f-04b44fba5929 | -10.1901 | -44.5703 | 2025-10-10 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 73717ce2-aa25-34e6-a4c0-461f002ffd97 | -8.9008 | -46.0007 | 2025-10-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| c84be9ad-8948-3dad-988f-7306afc13111 | -14.2749 | -45.8879 | 2025-10-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 78dc740e-cc31-37cc-beeb-3654f54e62d5 | -4.0567 | -42.5354 | 2025-10-10 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| db55b8be-cf86-3be3-84fb-3c1fc36ba8cd | -14.8628 | -48.4634 | 2025-10-10 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 5bce06da-550c-3d95-b2ec-7e645215e130 | -9.4677 | -45.9834 | 2025-10-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 17fb1fa1-20ed-303c-9cd8-dad5f301b2e8 | -8.2176 | -43.3873 | 2025-10-10 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 34130c84-5ec0-3eb1-9e9f-0ba41d2800c8 | -8.208 | -44.1337 | 2025-10-10 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 99858687-dcee-3724-9e57-bd5417629869 | -13.3026 | -47.1174 | 2025-10-10 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 97a42357-f009-31d6-970c-c4cce9733d63 | -16.7511 | -43.9887 | 2025-10-10 14:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 45c85846-5cf8-398d-953f-bab8d2008c44 | -7.5086 | -42.7329 | 2025-10-10 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 37e332c6-a694-3df6-9d2f-4dac75f18f61 | -10.1714 | -44.5496 | 2025-10-10 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6a2bc750-7f9c-33bd-b6a4-f0a4abc5d711 | -13.8307 | -45.8024 | 2025-10-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 341e7be5-7866-3aaa-910b-88f878c60dd2 | -9.4674 | -46.006 | 2025-10-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 1c1303e7-5969-3222-9ac2-4187dfcffb48 | -7.5277 | -44.2952 | 2025-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f03cd696-a008-399d-ba51-39ef37ec6c7d | -4.9526 | -42.833 | 2025-10-10 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 5fd12fe9-f864-3772-907e-ec1a7b8387e1 | -7.7922 | -44.2229 | 2025-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| b08c791e-9e79-3c34-9e34-81d2026ae455 | -7.1378 | -42.2006 | 2025-10-10 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 934685e3-23a4-3f1f-9112-7f92abf32588 | -9.2973 | -46.0026 | 2025-10-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 74da3d30-0921-3993-b0a5-a6b4592d6a23 | -9.4371 | -45.4656 | 2025-10-10 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 53eed7b8-02b0-34e0-8279-a972a8a8d024 | -8.8435 | -46.0519 | 2025-10-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| fc199602-b001-3f07-9eae-bf49d7226364 | -6.0799 | -42.5828 | 2025-10-10 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| c05b6895-2639-38d6-ba51-620dbad7b5d0 | -9.0022 | -45.4693 | 2025-10-10 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e947aea5-d5d3-3985-b8c9-e3a347a7e753 | -8.6106 | -45.102 | 2025-10-10 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f4e23a17-b37a-3052-8540-623993eefa5c | -8.2074 | -44.18 | 2025-10-10 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| fb05427b-1bf5-31ba-b4ea-a6cef4a81e73 | -6.0797 | -42.6064 | 2025-10-10 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| fc71b20d-635d-3f5e-9a40-ec662bc767d4 | -7.2959 | -44.8447 | 2025-10-10 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b3825470-274f-3588-b717-22f165740eed | -11.7221 | -45.3508 | 2025-10-10 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c7a7e217-27c1-3e60-b6f1-f808848e198a | -7.5466 | -44.2933 | 2025-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a9cbaa4b-9ea0-3da4-9b25-adbd7f88afac | -7.5275 | -44.3182 | 2025-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8d2b9863-417f-332b-9866-508d07563cca | -8.4844 | -46.134 | 2025-10-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 59564a9b-8a95-38a0-892b-cb78e929341f | -13.8491 | -45.8454 | 2025-10-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 76b0f629-9cde-3b35-a99d-01641e1e498a | -8.6109 | -45.0792 | 2025-10-10 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1ca52c3d-f5b5-3b7c-a7b9-039cc423e954 | -13.8311 | -45.7793 | 2025-10-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 166.4 |
| c14e13ba-917a-35e5-8781-c0fccc060b5e | -8.1618 | -43.323 | 2025-10-10 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 217.7 |
| 936a4bf1-e44b-3876-8fdd-e48a210d9a05 | -7.1345 | -44.1478 | 2025-10-10 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 67aea082-56ac-39c8-9eff-076487855071 | -13.8496 | -45.8223 | 2025-10-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6a933b3a-1849-3957-badc-df19bf81ad4f | -12.9619 | -46.808 | 2025-10-10 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 03fd2109-b31d-30f9-9a30-c1fcdb185c07 | -8.1615 | -43.3465 | 2025-10-10 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 491e0cb2-1680-3e95-8cc8-0fb14e9c90c2 | -14.4457 | -47.9719 | 2025-10-10 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3da1dbc3-32f0-3ae8-bb1c-c52ed2123c60 | -11.6278 | -47.5338 | 2025-10-10 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 86a56a46-2774-3c52-a8ab-b7c7dfdf217b | -8.5032 | -46.1321 | 2025-10-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 4729bac3-da20-3f38-be8f-86664c0c12bc | -12.4705 | -47.4416 | 2025-10-10 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9781d5e7-89fa-3795-9f48-084c1e3afe09 | -7.1347 | -44.1247 | 2025-10-10 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a8f3579b-2442-3a81-a6c9-5cc46ec3ce03 | -7.8648 | -44.4461 | 2025-10-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7ee8d95a-3b7f-36ca-85f0-8f91e8e55c39 | -7.5089 | -42.7093 | 2025-10-10 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 4109d104-db1d-3d1a-9603-f7b6cf81b16a | -10.1517 | -44.5984 | 2025-10-10 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0b1d9ddd-a929-33ba-920a-b9cedff94663 | -11.6278 | -47.5338 | 2025-10-10 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 54b5ad65-b67f-3e08-8860-dbf623a24076 | -7.5277 | -44.2952 | 2025-10-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ada7405e-0a1e-31b7-b4c1-e331686d4dc3 | -9.4371 | -45.4656 | 2025-10-10 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 73e4b14d-ff03-3d98-be74-fd0f791070ab | -16.7511 | -43.9887 | 2025-10-10 14:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 42845b67-74a1-35d5-942e-d7472dac4e36 | -4.9528 | -42.8095 | 2025-10-10 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 813c27cd-8da9-385f-9022-dc1b53573275 | -8.4824 | -46.2912 | 2025-10-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3e20b6fd-4c7a-312c-89f6-37f3f2cf6c37 | -7.2961 | -44.8218 | 2025-10-10 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c4441281-9565-351e-a4a4-bff327ce9a28 | -8.5055 | -45.9519 | 2025-10-10 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c1b5009d-83b1-3227-9cf1-b41ef24586c8 | -8.8807 | -46.0929 | 2025-10-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 31e85b94-9e29-3d24-84c5-3e52d0098780 | -8.8435 | -46.0519 | 2025-10-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 582d319a-2377-36c5-a07b-6ce4728a077d | -17.8216 | -57.6483 | 2025-10-10 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 6b78f13a-8dc9-30db-ba0c-8d7d456439c4 | -10.1711 | -44.5727 | 2025-10-10 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c9174bd0-7598-326f-9a22-b9f3d8c8fc7c | -8.1882 | -44.2052 | 2025-10-10 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 4c75849f-6430-338c-8af1-507e2cb990e1 | -7.8648 | -44.4461 | 2025-10-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fe409b22-c6d4-3a50-a341-4ee22e525164 | -7.5466 | -44.2933 | 2025-10-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |


[Clique aqui para ver as próximas entradas](README56.md)
