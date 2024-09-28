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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ba52ffa-2b3d-3bdf-ae38-94c4d65862ec | -16.57815 | -46.9314 | 2024-09-28 05:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dd94e7d-28ce-3528-b96a-6915b3748af1 | -10.6495 | -46.05822 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 64c08dd4-3e9c-38bc-bddb-0e53db5ecd42 | -10.64889 | -46.06341 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c87ad012-50c5-38a5-8c21-32efa32d8fe2 | -10.64828 | -46.06858 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 299e1f0f-414e-39d8-ba9d-7138611054cb | -10.64429 | -46.04701 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2037b54c-e0a4-335b-9378-b3cedfa9af65 | -10.64368 | -46.05214 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5c5f2d0e-0541-335b-9766-0f67f64fe1a1 | -10.64307 | -46.0573 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c3ff8f49-c627-3247-aed8-cdd5b89ddda3 | -10.64185 | -46.06765 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9bf85b69-edcc-3861-b193-752c7813edbd | -10.64124 | -46.07283 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 040f29ce-74c3-3e18-8b4c-8ff5a7f267bf | -10.64062 | -46.07807 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ed71376-0ff1-39da-96c0-38158bace64c | -10.63783 | -46.04625 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 11a388ab-db65-3bf7-8f9e-d590b2c395bf | -10.63723 | -46.05133 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f7b1a45-986a-39c2-b98b-ad112174691c | -10.63693 | -46.0476 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cef6cb0a-b8e9-3196-ae97-6b90b6682e35 | -10.63663 | -46.05644 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4e721fe7-b1f1-322a-af93-047231ae7ab6 | -10.6363 | -46.05267 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd8587cd-33d0-3c8d-9b6d-a378110a57f3 | -10.63603 | -46.0616 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 954f5370-e98b-37c1-b408-edaf6cfadc31 | -10.63542 | -46.06679 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| edf3f5f9-306f-3090-85da-784fe9a88e7d | -10.63503 | -46.06293 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7e0b90c-862e-33d9-b8f3-0a76acb17003 | -10.6348 | -46.07203 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07cd7ee2-407d-3848-b4a7-76a0cc456b32 | -10.63417 | -46.0774 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49d3f3ff-6fd3-39b7-93df-90d88cbeb7a7 | -10.63373 | -46.07342 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8ace26e-880a-30e7-99ed-e841adab86c0 | -10.63306 | -46.0788 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f56bbb7d-b965-3f64-b310-0a26bd68745c | -10.62834 | -46.07138 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72a7b629-160b-333f-837e-205dcb0df24e | -10.6277 | -46.07688 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13dbbe8a-05ce-37ca-83fc-e96b14039af4 | -10.62726 | -46.07283 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32b671f4-6f1e-38ad-a339-b847ac5cb227 | -10.62187 | -46.07084 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53ac91b5-0829-32a5-9b5e-f7657049ac66 | -10.62145 | -46.06697 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9977b2cc-ba5e-393a-8e7e-e7cb05b534d0 | -10.61601 | -46.06507 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a52ff71-e85a-356e-87b9-4280b357204d | -10.61561 | -46.0613 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a89dbb9-6d20-3740-8525-0d3a9117e518 | -10.61497 | -46.06654 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 832ca637-7ed0-3a71-869a-0fc8e76b6d68 | -10.59722 | -46.05804 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a24be2c8-df71-3084-bc22-955da1e54d0a | -10.59201 | -46.04644 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 958d928c-9995-3832-8dd6-472aa308bf9d | -10.59661 | -46.06334 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98dbb2ec-561b-30ca-a70c-1c7dca41c556 | -10.59621 | -46.05955 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 856acbff-2696-33e2-9f4a-87bf710440c9 | -10.59602 | -46.0685 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7f7d3fa-96c3-35bb-98a3-464bfad814cc | -10.59557 | -46.06479 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7451e5a1-9c67-32da-8004-22dfe8221c32 | -10.5827 | -46.06313 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56a38ea5-d492-3b11-94f4-2226cd88a437 | -10.57626 | -46.06234 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b75c380e-306d-327c-9675-d3dc719d759f | -10.57564 | -46.06747 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d22d0e4a-601b-3687-a6c9-374173ce834c | -10.57503 | -46.0726 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 123be2d2-c359-3f75-a754-f098ed0359b0 | -10.57441 | -46.07771 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2782ef6-d580-3e2b-861e-52859ac76bd2 | -10.57379 | -46.08287 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5129cb39-9f69-3510-9568-e097ab005133 | -10.57316 | -46.08805 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81196913-850e-3867-ae01-8c504f546c9e | -10.57253 | -46.0933 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49a2a5ca-2b04-30a1-af17-e9901f8c9c44 | -10.5719 | -46.09847 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d8d520e-34dd-3a1a-8369-bba586a23dbd | -10.57128 | -46.10358 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03c9597e-ae60-3d05-bd6b-128f7fe2ac7d | -10.57045 | -46.05632 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d2c4c5db-4a62-3d87-b9ca-51a7ef098e1a | -10.56983 | -46.06152 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 08221963-b4ce-3182-9357-f46489bafb45 | -10.56921 | -46.0667 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dcfb390f-5695-351d-84ad-d7a3c8fcf4bc | -10.56468 | -46.04995 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 99ac1364-2e33-3a1a-8ca7-dd8586566f5a | -10.56405 | -46.05517 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 41a64d9c-0f65-3158-8812-e20458f622d9 | -10.55827 | -46.04891 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02163ae3-2464-35c1-87a8-736d4edb4887 | -10.89903 | -46.41261 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4960130f-cfe2-3c1c-b1cc-594e2cd2fc24 | -10.89564 | -46.41441 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe7cfc10-7e54-39e3-a3fe-330757bdbf3f | -10.89268 | -46.41196 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c24d234-bff6-3b3d-9020-84f301c9e89a | -10.8854 | -46.39318 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 57e80d83-e3da-3464-bbd6-2eeca48314f9 | -10.88232 | -46.39047 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b5b68a5d-49bd-32a9-b9ab-9380f73d9a42 | -10.8797 | -46.38718 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9cd6d8f5-58a9-33cc-aa9a-a76aebfb47fe | -10.87908 | -46.39232 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da4e53f9-14dd-3b7e-afb5-231451ed3b79 | -10.87601 | -46.3895 | 2024-09-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd381598-f3ad-3142-9dd9-a728f4d9a03e | -11.07632 | -46.13058 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3070ec67-f9e8-3515-9a53-16677adceada | -11.07568 | -46.13607 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eec2cf0d-271d-3350-86c0-6cecc70a700a | -15.62961 | -47.2308 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 35a71465-50ba-3255-b3ba-7522df1ce347 | -15.62906 | -47.23646 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fe012b1e-210d-3ca0-aac6-1dbb1cbdb700 | -15.62854 | -47.24179 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cdfebb7-704b-39bf-a4a7-893463806add | -15.62739 | -47.22779 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| db322799-e46d-3791-bc11-e3cb0a3f46ea | -15.62681 | -47.23344 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| da24f4dd-059c-3ea2-be5d-0b7b8057688b | -15.62623 | -47.239 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9cfee9e4-00b9-35be-897d-4b76f0ce328b | -15.62105 | -47.22696 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49ff788f-5b0c-3e8d-a94a-5772360f7fa2 | -15.62046 | -47.23259 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 89d5118a-fe9b-3dc1-a77e-a65b6f4ed8e7 | -15.61413 | -47.23158 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a8a42b4-0097-37d5-ae61-39f828e9712c | -15.41157 | -47.45573 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd24244b-26ca-3649-9c3d-7e8ee8ed89f3 | -15.40981 | -47.45295 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f3f4d62-43e8-3da9-91ef-35ef0f32c7df | -15.40537 | -47.45443 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8bfd184-8550-34d7-9d7e-2d387ca9db7e | -15.40361 | -47.45164 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 135faa76-f8a1-3b20-ba39-066f1ba499ab | -15.37333 | -47.45804 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc996d6f-0414-3046-a20d-87930c1fd48f | -15.37269 | -47.4641 | 2024-09-28 05:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc772282-cc9d-32c2-ad31-f3c9d3984976 | -15.31401 | -48.01622 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4f65e82-db6e-3f64-8c93-bca405703809 | -15.30954 | -48.00084 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a6c9c86-46bf-3900-b279-5dcd7d92d13e | -15.30903 | -48.00565 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a5958a3-4935-38fb-8ed8-e9224b1b2af4 | -15.30849 | -48.01073 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1eb4c4e5-9f6c-303c-ab66-dd252114309b | -15.30798 | -48.01542 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66741fdb-b450-3aa8-aeea-192787a6f6ba | -15.26553 | -48.29772 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47d4ccbd-16e3-3ae0-bfce-c58ed3877c09 | -15.25958 | -48.29718 | 2024-09-28 05:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 67a5eb1c-9b29-3fa4-acd2-2e7411aaaa71 | -10.6788 | -47.95258 | 2024-09-28 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e469120-29b3-3c0d-b7d4-be844b29d61a | -13.48038 | -48.57956 | 2024-09-28 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4cb9093-8d58-3499-8458-e04622203455 | -13.48001 | -48.58287 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c108963-f816-3953-b97a-efe40198375f | -13.47114 | -48.59199 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2df2bb52-3b9b-3cac-a1c7-53b218695ac5 | -13.46492 | -48.59572 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4cc739f-09ea-34e0-b2dc-1a2ef2945e32 | -13.45925 | -48.59491 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2ca42d7-bdc4-340b-838c-1af0c99dfe90 | -13.45542 | -48.57836 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e45b3b4-8aaa-3a4b-a5e7-f8629b78db24 | -13.45499 | -48.58203 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b21ee4a9-b5cf-3e88-a0d0-f2c2263c9009 | -13.45455 | -48.58578 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a3f5442-6e31-334c-93e9-ecff454421fb | -13.4541 | -48.5896 | 2024-09-28 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c54ead67-302d-3f0b-a402-efd09d038460 | -13.16657 | -48.54058 | 2024-09-28 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff1cc14a-88ae-3dbf-bba3-4a3e1994a089 | -13.1641 | -48.54065 | 2024-09-28 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b9c1fb6-03c4-39f3-ade7-2790304ed1a4 | -13.15799 | -48.54348 | 2024-09-28 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5915fdd9-8087-3e17-859e-e4563980ec63 | -13.02708 | -48.60658 | 2024-09-28 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47b5e4d9-abec-320e-b8f8-e26e83102aed | -13.02658 | -48.61077 | 2024-09-28 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcc83b05-5e80-3af8-8049-9afc6279ac9f | -13.02157 | -48.60467 | 2024-09-28 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README77.md)
