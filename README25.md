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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 771bf87c-9f44-3961-ad59-1eb6a9edc5a4 | -12.76471 | -39.54917 | 2024-10-29 03:47:00 | NOAA-20 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0a3e2197-3ad7-3654-b2ce-f8579e9d531b | -12.76412 | -39.55279 | 2024-10-29 03:47:00 | NOAA-20 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3485f66d-3793-3dcd-a820-2784be3b7d28 | -6.41797 | -39.79934 | 2024-10-29 03:47:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3512f536-68b0-3b73-9e08-4bdf2dfd6358 | -5.93477 | -39.47348 | 2024-10-29 03:47:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 58c17adf-5664-3673-bde7-1d7ee3490c95 | -5.93412 | -39.47748 | 2024-10-29 03:47:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e6ba0e3e-e280-3156-b219-19671da0abef | -5.93058 | -39.47691 | 2024-10-29 03:47:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eca3c60c-cc3f-30f7-95f1-0bc49a65164e | -7.32653 | -39.36544 | 2024-10-29 03:47:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4470668e-9134-32cd-81ae-1c5c81c9236c | -7.28373 | -39.73586 | 2024-10-29 03:47:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22c71e77-b5f7-38f5-9fa2-75907cf70dd2 | -7.0873 | -40.58958 | 2024-10-29 03:47:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 496a77fd-f7a6-3251-aadc-6a6b780d4804 | -6.63083 | -39.71574 | 2024-10-29 03:47:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed6f4f41-8e53-32f0-8d9a-c65faf8cdaee | -13.01415 | -40.59306 | 2024-10-29 03:47:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26f3ea2d-a08b-3b6b-bc53-5fa08e32d926 | -14.01019 | -41.01714 | 2024-10-29 03:47:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4894cfed-d831-3461-bfe0-dae62ca90a72 | -14.00671 | -41.01653 | 2024-10-29 03:47:00 | NOAA-20 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcee1d8d-f0f1-34e4-ab6a-15c8425f293e | -3.59121 | -40.33403 | 2024-10-29 03:47:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a06cf29e-a537-3a92-a5b5-45f53e7c24cf | -3.58739 | -40.33342 | 2024-10-29 03:47:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8144c8eb-d8b0-3bda-859d-06aeb6ee3ad6 | -3.1656 | -40.20831 | 2024-10-29 03:47:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 06f3f7ac-f9d4-3541-8b47-5c48f03da585 | -4.40872 | -40.69529 | 2024-10-29 03:47:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a858ee69-460d-314e-a8d8-312ef1d8006d | -4.40477 | -40.71928 | 2024-10-29 03:47:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 780b5d4d-0f02-360b-8326-9875e5c0f406 | -3.89149 | -41.03569 | 2024-10-29 03:47:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a03956d-075c-31f6-b0aa-ca9a46c79a31 | -3.88981 | -41.0369 | 2024-10-29 03:47:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b931d4e6-5bbc-37ba-adcc-9fe7311ce27f | -3.85242 | -40.70333 | 2024-10-29 03:47:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f1f154c-e044-398a-aaf1-758212e9e4d2 | -3.80158 | -40.96278 | 2024-10-29 03:47:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e461258-2616-3679-997f-963866567542 | -3.79836 | -40.96556 | 2024-10-29 03:47:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 625904ed-6ca0-37f9-877c-743b76b80182 | -6.36319 | -41.57248 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a224b32-8bb8-3712-81c2-cb49e1775a3b | -6.35921 | -41.57193 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed73ef1f-fc4b-3e4a-977f-f5dad39d5dd0 | -6.35835 | -41.57713 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f4cceb5-0bf1-3d9e-8baf-a848a792b5d4 | -6.35751 | -41.58221 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 548bdecc-0bbe-387a-8984-8909339f4d2b | -6.35438 | -41.57654 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 065644fb-a17a-31fe-948f-9e6a39c15b2c | -6.35353 | -41.58164 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 875c5dcf-70c4-30b7-ac34-3233aa0771e4 | -6.35187 | -41.59166 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6bea30e-9bae-39fc-b3f5-4da3ee8dde9c | -6.35104 | -41.59668 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0995484-918c-303c-b627-a4cf7f5220ba | -6.34956 | -41.58103 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 24c71261-0a09-3663-94b9-99007431adc0 | -6.30163 | -41.91909 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dc6b514-cf5b-3d81-852e-f1dbcc37285e | -6.30103 | -41.92271 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51624fba-ff71-3349-93ac-f86bcb4babe4 | -6.28705 | -41.93156 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a602562a-22e1-31b1-9f4f-a6460ec5bc38 | -6.28643 | -41.93527 | 2024-10-29 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfcfa422-abc7-317e-9d7b-8490dd643181 | -6.15983 | -41.86939 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0718899c-ab9e-324b-8784-65dfce531d4f | -6.15645 | -41.86477 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 69992ead-6925-33b0-ad30-2e05399830d9 | -6.15585 | -41.86832 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 279fbaec-905d-3f7c-bcc0-f5e4678f2550 | -6.15522 | -41.87201 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a3344aae-ee41-332c-9696-b058d342bcb3 | -6.15301 | -41.86044 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e2ee700b-60b8-35b6-aadc-cf61d2b93648 | -6.15243 | -41.86389 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c4be852b-8c79-3f86-8e51-56fad4e05e83 | -6.1518 | -41.8676 | 2024-10-29 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58d1d583-cf11-3e7f-baad-b19727a17696 | -5.62267 | -41.73599 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14ad9a6d-96e5-371f-b643-9af88df3c9ee | -5.61925 | -41.73165 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 680c6ecb-31dd-3a95-903d-f356ef00c05b | -5.61893 | -41.73191 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 478b3fc6-73a1-337d-9422-ee6dd6bcec8a | -5.61863 | -41.73526 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dd2b26e3-5296-3790-8372-56bfb73422a1 | -5.61835 | -41.73553 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 404905a5-a371-3cd2-b9e0-7554658f85d3 | -5.6152 | -41.73096 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c35fcb1-dbe3-32ef-82f2-e1e2710c1cd2 | -5.61489 | -41.73122 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67079bf3-dc44-36f0-8189-8e78106aa2c5 | -5.60672 | -41.75589 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 78678089-f209-38e8-b3ea-d253212f600c | -5.60275 | -41.72915 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 18fd2d97-25a7-3e87-aad2-f27610b39a95 | -5.59868 | -41.72857 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 706bebec-0d91-3322-bd84-00ac7ba4e976 | -5.46769 | -40.88408 | 2024-10-29 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0347ab80-c74d-328a-8048-ce8db043f00d | -5.46695 | -40.88857 | 2024-10-29 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 55e8932c-5739-3495-aea1-ba6262777b97 | -5.40322 | -41.42109 | 2024-10-29 03:47:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e87e4b7-2f35-37b3-8e2e-8dca34d15635 | -5.40264 | -41.42464 | 2024-10-29 03:47:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 082f52ae-a0ee-3765-a067-7638e4a85e87 | -5.26021 | -41.24157 | 2024-10-29 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0d5a369a-b486-3b6a-992e-763176a93359 | -5.25989 | -41.2381 | 2024-10-29 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0e824efe-15d4-384b-9fa2-a07e752a1b47 | -13.24668 | -42.80467 | 2024-10-29 03:47:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a20ada7-6a60-3677-98c0-d02de843b04f | -5.01691 | -41.71364 | 2024-10-29 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfd6b163-861e-3e30-a9b3-5d78d9e58ef2 | -7.33756 | -41.87331 | 2024-10-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2852ba9c-b52e-3460-95cc-c9f6612cd385 | -7.33021 | -41.86843 | 2024-10-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d55962f5-ccf4-318f-a7a8-3495c17a2d4a | -7.3296 | -41.87195 | 2024-10-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8523c43-a61a-34a9-9b36-664b9c2ed0fe | -7.329 | -41.87547 | 2024-10-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78bcdd16-fa50-354a-95d5-df4a9d078bb1 | -7.32142 | -42.18677 | 2024-10-29 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2c9bbfd-2056-336a-b87c-66878b165d13 | -7.31737 | -42.18607 | 2024-10-29 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d6cbfc6c-37c8-30db-bb57-9c6b43b6ed3a | -7.00917 | -41.2947 | 2024-10-29 03:47:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7a8f2eff-79ca-3006-9ad3-6d65fc5178e9 | -7.00834 | -41.29958 | 2024-10-29 03:47:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f19c3762-d51d-3a1c-b025-53d47866da21 | -6.99704 | -41.34296 | 2024-10-29 03:47:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 75b254d2-8e9c-379f-ada8-b1d1fba06a1f | -6.99485 | -41.33243 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8cf99b5d-ad81-358a-ba31-227f66940218 | -6.99401 | -41.33736 | 2024-10-29 03:47:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2070142b-2744-34a6-a274-75f20cd75495 | -6.99385 | -41.33102 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b29e1d80-303b-3fe3-9c1a-a7827354bab3 | -6.99305 | -41.33596 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ef08bdc1-b3b2-3580-95f4-0d31ce9c22ff | -6.99224 | -41.34093 | 2024-10-29 03:47:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e9d3487b-64c8-35a7-9842-9ae78daa85a4 | -6.99181 | -41.32687 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 644a0d0d-7145-3218-8681-962221f6a786 | -6.99078 | -41.32545 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fecc7510-4893-3a4f-8693-03b3a416fc8f | -6.99014 | -41.33674 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eacca5d2-84e9-322a-9129-2eb720ca4629 | -6.98918 | -41.33533 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 85a08928-7f42-3ee3-afdf-b3f75d04be8a | -6.98711 | -41.33118 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe941e6d-6667-3fe5-af7d-d8897c5de662 | -6.98627 | -41.33613 | 2024-10-29 03:47:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f4299263-3f7f-375c-b817-4ba9a81ddff6 | -6.67623 | -40.89684 | 2024-10-29 03:47:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbe87b24-7ec4-3732-bba5-cda73e1d1e3e | -6.67321 | -40.89159 | 2024-10-29 03:47:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0752f38-91cd-32a6-9ab6-4ab8d7c6a857 | -6.51543 | -41.57929 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f64b0491-ed55-35e7-b97b-add3b9b854a0 | -12.00933 | -42.94909 | 2024-10-29 03:47:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9595be73-709a-30d6-8848-10c5feacef8d | -12.00537 | -42.94838 | 2024-10-29 03:47:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| da753c4a-1ccf-388f-9070-17e86da53f3c | -11.29024 | -41.86273 | 2024-10-29 03:47:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8dd267e9-91da-32bd-ad73-caff45b08a13 | -11.28649 | -41.86209 | 2024-10-29 03:47:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6df545bb-9914-36b9-a55e-b71f2f7f7681 | -13.55433 | -43.42177 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c4307b0-4033-36bf-beaf-ebc443d1ad5d | -13.25054 | -42.80532 | 2024-10-29 03:47:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ef06ef2-67fb-357a-a401-888766c218c5 | -13.13126 | -42.43419 | 2024-10-29 03:47:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3eb20848-5cce-3fbc-9810-a59662eb4feb | -12.64709 | -43.25671 | 2024-10-29 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2e3626c-3a1e-37f2-966d-0dee5ad98e2a | -13.7937 | -43.25149 | 2024-10-29 03:47:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b55d351f-8635-3cf9-a8a6-7e0f53317682 | -13.78677 | -42.89525 | 2024-10-29 03:47:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa13c59d-8651-3c3a-8e0f-35b6a9348dee | -13.7616 | -43.11389 | 2024-10-29 03:47:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b47fe36-6cec-30b5-8fdd-d63857f8ff06 | -3.39391 | -41.61392 | 2024-10-29 03:47:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39f88123-968b-33c8-ba7a-6cbbb2ecde71 | -3.39036 | -41.60951 | 2024-10-29 03:47:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8fc5e0b1-5848-341e-8ca0-7c639297f8c5 | -4.98727 | -42.28685 | 2024-10-29 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9f0426c-ef9f-33ff-bd0e-2aaa033cd1c8 | -4.98686 | -42.28627 | 2024-10-29 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 747e53a0-b1ca-3578-99e1-0d24e2407ebc | -4.98366 | -42.28222 | 2024-10-29 03:47:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README26.md)
