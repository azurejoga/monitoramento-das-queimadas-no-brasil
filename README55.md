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
| b55c1861-3162-302f-ad68-a4ae3261894c | -3.45045 | -50.60568 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d36c7b1e-50d6-3249-9b94-720e87b58715 | -4.68062 | -55.62922 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2894ba08-43dc-3e19-abcc-8e11b21ae54b | -3.76908 | -59.18824 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0158182e-fdd7-3031-9c1c-44e6f898d57f | -3.07301 | -61.27246 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9957579e-fc33-340e-a82b-67a1152cb597 | -3.18952 | -60.43344 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5607c00e-86e7-370f-924d-2996a169f475 | -4.56217 | -56.14734 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fd309ae-ec83-36bb-b6f5-8826a6160407 | -3.76993 | -56.79285 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31628f56-69f2-397d-9a67-305487854310 | -4.5665 | -55.74885 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60de69c2-f150-32e4-93b7-6cc7cbfcc8e1 | -3.69032 | -60.59106 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43bbb0cc-5a2f-3f7f-b69d-042d195341c5 | -6.91559 | -43.73399 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c066b26-47f8-3b19-8083-dc7e7efd5c8f | -5.82264 | -52.1152 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48fd3dee-a63e-3885-9bac-5c4b13861cd9 | -4.26124 | -55.76412 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9b74ee-9cde-3223-9d8f-39b230e40e42 | -4.3527 | -55.6587 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fe56f90-9663-38a7-a626-70daf5d7dc38 | -6.72864 | -55.07684 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 197f313e-9b11-3231-afcb-725105146d08 | -6.35511 | -55.86486 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51b5d9b0-f3ef-3402-a1d0-5f2baa0bf5e3 | -2.64634 | -54.69048 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 56dc3fc8-d0a5-3b4a-8d75-34da69b31c9f | -5.82459 | -53.51087 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1753b09e-c0db-3ba6-93a1-1b527e1522df | -7.41718 | -44.77557 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f1a02695-b78c-3d3c-829b-09e2fd205b44 | -3.49128 | -59.607 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 102c1aaf-a28c-3226-8eba-2ba160e6346b | -5.91968 | -57.67916 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a15458a-3f9b-3cac-bdcf-ac69e2a4af93 | -6.19495 | -55.45097 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c3b476-0f47-37f3-b1f0-def5c837968d | -6.13909 | -59.94978 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1c00309-543b-3ea2-b40f-fd95f47d4bd3 | -3.45499 | -50.60498 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 554a6ba4-5d8a-3513-99be-bd087d11cc45 | -4.35324 | -55.65527 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c525b08-3af7-3290-80dc-8fa16f523046 | -8.30612 | -45.99987 | 2026-09-21 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9bc84d4-d9d6-3d59-95ce-2df592feba15 | -4.04814 | -55.71273 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aca4186-9b72-380e-98c7-1c7b262391a7 | -5.85235 | -53.53042 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0b985d-0393-34cd-912c-8d5805e6c6a0 | -6.45023 | -57.87602 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e3ab951-13f5-3293-aba9-6e7eff379cac | -6.19397 | -55.47916 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c0edf7-5f07-32ef-8d12-6a8fef34c347 | -3.3988 | -59.58012 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7946befc-b3af-3890-bdd0-f03e088734d9 | -5.83671 | -53.49268 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1535ff4-e627-3e01-bb2d-2ac4ec0a9cae | -6.21384 | -57.72953 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c1e73d9-f434-31d6-a8a7-a3a794ee7860 | -6.11612 | -57.74743 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4eddc9d-1a71-30db-b028-074ee4ac89fa | -4.80748 | -56.07988 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7389dc18-ed7f-3a39-ad49-54236f13dcf7 | -1.6789 | -54.93614 | 2026-09-21 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a51a1a7b-c3b6-3c2b-a31b-d9eb33eed9b5 | -3.39088 | -50.43953 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aced51a6-67bd-3122-a45e-3c9a079dfaba | -1.91473 | -58.26186 | 2026-09-21 05:04:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a2c156-9335-3e57-8340-6ec66d905b0e | -6.21226 | -53.56356 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50a5a7a4-fba6-3065-8c53-260f3c751c6c | -3.82682 | -59.33163 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1f92744-c24d-3e2c-8597-df1fd434f416 | -5.76955 | -57.58769 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 249679bd-9008-3d83-b0f1-25a14a8e068a | -6.73638 | -55.07083 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80d23dcb-3bb0-3910-94a7-9d0cc8aab1f0 | -3.34548 | -59.8604 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88a6e802-a4f1-3da3-8e8a-ec89db12cebd | -3.48212 | -59.56657 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a95f4e2-46c3-376d-9141-917151c9e2f7 | -6.91634 | -43.72845 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 821ef4ff-156b-388f-b680-6128523df5aa | -6.13723 | -57.72437 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1fe379d-ce8f-3654-9cee-3a0a4e8d9fbe | -3.34317 | -59.8499 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a8accfe-4f6a-31e0-a22d-c799ef407ff2 | -5.27584 | -49.34472 | 2026-09-21 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9675a1d-9032-3411-974c-6a215ba83a40 | -7.38612 | -51.77523 | 2026-09-21 05:04:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d18b9fdb-5220-3938-818e-4c713bc1fd0b | -2.91032 | -57.78645 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 30a305c8-5edd-38ae-a947-13d312862b7c | -5.86157 | -53.49275 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8fa575e-c432-3de0-8502-90ca6929c987 | -6.53868 | -44.93154 | 2026-09-21 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7e2f2c7-9cc3-30f4-82e2-4da9041e0d46 | -2.78866 | -59.89339 | 2026-09-21 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd34082a-33aa-347d-857a-5c75308c170b | -5.99606 | -53.64922 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91252b96-d6cf-3cfa-bf05-05316b469479 | -5.2643 | -55.92229 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5f43267-fade-3dbe-b645-c15f84acb595 | -5.97459 | -55.35604 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be4575de-e1c7-3d00-a32b-9a777c25fe60 | -5.84193 | -53.50527 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 284578d9-63f5-3211-8722-a7bdff0e4298 | -5.86376 | -51.93772 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16673cf4-2af5-3546-a9d2-b06d6f19f793 | -2.8767 | -57.78926 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c1c2577-be58-3864-9db7-c0ae786148d5 | -2.1716 | -48.32565 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 150fc7dd-f59a-3384-893a-22dedae2cd12 | -5.81936 | -53.52185 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d661b29a-977d-3087-a419-c620373d8854 | -6.41859 | -55.01446 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c81e3e7-c365-3385-bdde-1a62de5c121a | -5.84946 | -53.52605 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb7e1f8b-51fb-3f4b-9c93-339156e15902 | -2.2943 | -48.59611 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cb3f654-b252-3493-8a88-fa7cd4890847 | -3.33305 | -59.83826 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3db69299-418a-3b39-bb47-57389f57eb02 | -8.00665 | -44.81283 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cbefe446-3d7a-3e1a-8009-f74297a1cb51 | -3.45578 | -50.59987 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22ab8c4b-1eb6-3c40-a885-217c568b8158 | -5.75713 | -57.57821 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 098a14f5-a935-34e1-a04c-22169fc50062 | -5.99064 | -57.69783 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e712748d-0825-3408-a2bf-ddf94ea6d680 | -4.49518 | -55.48717 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2f2b18e-c216-3737-9596-a8eea1743abc | -6.73862 | -55.07841 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef087d77-d58f-3a8d-a36c-2814a5164e0a | -3.01401 | -54.18289 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25494bfd-e53c-3773-80e5-93befa7d9347 | -3.01271 | -54.172 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7f1140a-14d7-32b4-a88b-1d072cf7dfb6 | -4.55886 | -56.14682 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d0ff402-e96d-3dbe-b1a9-5aa7f6906857 | -6.19602 | -55.44405 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c3f52ab-299b-3c0b-a123-3c131506e33e | -2.95835 | -57.71006 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 492bc316-a370-3fdf-b0a3-f77379007dcd | -3.29154 | -59.44959 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da22f29b-66fc-3f08-83a5-bf82fc415993 | -6.1572 | -57.95213 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e5ad6eb-71f7-3f20-adf3-5b91bd7357d0 | -5.75936 | -57.58606 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c004af9-d3ee-33ba-9d15-34b1a600f5e9 | -8.30792 | -46.86959 | 2026-09-21 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95e58c5d-a9ab-32de-af24-0a37af76ab7f | -5.8617 | -52.03039 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e83afe30-4bf1-3f94-9d91-7df5e3afc5a3 | -5.83795 | -53.49328 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e743efc-b30e-3f8a-ab51-b13c6dbe321d | -5.88588 | -52.04753 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e87bbf81-39b6-3f34-98e7-9b208f8293aa | -3.35864 | -50.44826 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e5306fc-3b90-3487-9066-ac66efaa792f | -5.8842 | -57.72655 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4fa956c-2b73-34e9-bef9-083ffe048137 | -6.15715 | -57.70869 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d03cff6f-5dd0-3b6b-8b3e-436838eebaa1 | -6.92672 | -55.62232 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e70e1f92-2c71-30bf-8911-1d0045964659 | -7.42462 | -44.7667 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f78dadd3-e45e-3abb-9889-a59539c377fa | -5.98012 | -55.36401 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 323dd0e0-838e-3833-86b9-581c9b1aac3a | -7.42207 | -44.78651 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca16be42-3684-34b9-9b37-62c430767236 | -3.45421 | -50.61007 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ce552fe-2bfe-3320-90c1-eabc1cbd3887 | -2.95713 | -57.71782 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6be9ba8-8924-3beb-8eff-4e79e74cd941 | -5.22188 | -56.1064 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe847f57-55d2-322d-99c7-633c4d2c3254 | -6.14097 | -55.70736 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffaa10d2-a381-3db3-b0dd-96fa10379374 | -6.3617 | -43.36036 | 2026-09-21 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 725b3a76-d36a-3a0d-9268-2ea12bdbae9d | -6.90851 | -43.72985 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc9d8fb5-7fb8-39f9-8e9d-943e5dec4122 | -4.35047 | -55.65132 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbc0827f-f0e9-3d8a-92c1-0c598435af3e | -5.84023 | -53.5403 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8bbb97-0c4b-3663-ae89-cc66466310ba | -3.39881 | -59.53147 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea74a60e-44ba-3176-8a9d-c9819f87b414 | -3.59464 | -59.06317 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 374b2771-957a-301b-9777-d8316eb0aaf1 | -3.00883 | -54.17498 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)
