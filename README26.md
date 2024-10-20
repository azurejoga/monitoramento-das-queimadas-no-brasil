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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7d08b7-73e5-3a6e-b376-6b60e7c54098 | -2.51146 | -45.99497 | 2024-10-20 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 270cf18a-d109-351f-9ca2-4d1653d74bdf | -3.51112 | -46.22842 | 2024-10-20 04:29:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c58a8d30-e8f8-3dac-bc1c-a6f9d25e0a88 | -3.51056 | -46.23193 | 2024-10-20 04:29:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07fef8a7-1048-33b8-925d-0ec7bde813ef | -3.37467 | -46.49313 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23e49566-021b-30b1-bbd3-3656b8674140 | -3.37188 | -46.48917 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 054c6309-f56f-319f-8e0e-b506ec2ab278 | -3.37133 | -46.49263 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bf2e6ec-7b65-3711-920b-e4c4cadf0f68 | -3.23332 | -46.50976 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a82ef46-d738-386d-a06f-89416b6120ef | -3.23278 | -46.51323 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 148f4db7-11bd-3461-b4d2-348e1f5a2b43 | -3.23 | -46.50925 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95ca72a9-12ea-3c08-b53c-3c82bf853ba0 | -3.0877 | -46.55103 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 745273e3-940f-3d7a-83d3-7ccde2af93a0 | -3.08715 | -46.55449 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e52583a1-952b-3813-ba75-a2016b42db4a | -3.07297 | -46.62317 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b3db5b1-4494-37b1-ba60-e3d9ff2b3d24 | -2.6291 | -46.9073 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aca734e2-9403-3e7c-9e9c-d10489104d7f | -2.62855 | -46.91074 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ea12156-38fc-379e-a328-3dbf0cef7e6e | -2.62578 | -46.90678 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd86f4e-687d-39a1-9179-be92eca66a12 | -2.62523 | -46.91023 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50926b65-bf6e-31b5-9da5-3165f30316f2 | -2.44429 | -46.89983 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d370eda4-2f6a-3c6e-ac6f-f9b4a9283907 | -2.44097 | -46.89931 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df08cb3a-835f-3480-a0b5-6138442fe77f | -2.44043 | -46.90276 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4536917c-b5d1-33ab-8f8b-ef1decb112e4 | -2.40835 | -46.71771 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 975bdc3e-ee0f-3b24-81f5-afbf0535e6f4 | -2.40666 | -46.70685 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fdd816b-10ff-359b-b788-51d87f839a57 | -2.40557 | -46.71375 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efac83d5-ae97-399c-a556-c3705310cf6f | -2.40503 | -46.7172 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b667369-b9d7-3417-bef3-6fc625641050 | -2.40334 | -46.70634 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33adb353-d592-31b6-b7e9-13484b1808f9 | -2.40225 | -46.71323 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 187eb2d7-7530-3ee7-85d6-ced3e1c4ecd7 | -2.40056 | -46.70237 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd5e79a1-b5cb-39d5-b62a-385061d91822 | -2.39785 | -46.71962 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 163385b5-795a-30c8-a82d-bda94c9773a2 | -2.39453 | -46.7191 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d74f58e4-0531-33d5-b44d-8382825ce467 | -2.36195 | -46.47736 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa409bc0-ffcb-3894-a25a-888bc3b7a993 | -2.33979 | -46.83428 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04ef58b5-9bc8-3628-9dbb-e71183e91b99 | -2.32356 | -46.59163 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e61f9ea-f1d9-36d7-9764-73baa1266610 | -2.32172 | -46.71145 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b38939c9-2833-3886-bf4e-2874ec886342 | -2.3184 | -46.71093 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54d27cff-3cbd-3950-9903-4372e9b56a8b | -2.31508 | -46.71042 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de80926b-7578-3f97-9a34-1ee1b348a4a3 | -2.31252 | -46.59698 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6e32633-7526-38fa-a99e-4f08cca50c4f | -2.26875 | -46.74557 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47768c4f-58d0-3332-b384-bba9928a78a7 | -2.2676 | -46.73128 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6b941ac-0aec-3c2d-8120-588b0d687088 | -2.26597 | -46.74162 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eccd4759-f190-3e66-a0bf-f5c7b8637a68 | -2.26543 | -46.74506 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a3eb7a3-41d0-37f3-97e8-f8474ab1ab46 | -2.26265 | -46.7411 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a3c8708-965d-3596-b706-244f8e459c63 | -2.26163 | -46.76918 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ac4779b-2aa5-3f6a-9069-33904fefb7d3 | -2.2615 | -46.7268 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 936a03cc-c7df-3945-96a1-f5a0bc1f1bf7 | -2.26042 | -46.73369 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7adb67c-156b-3ab6-93ec-7e570e86cea4 | -2.25988 | -46.73714 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32d9ca43-4970-3a80-a33c-67b755fb974b | -2.25933 | -46.74058 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ac16c5f-2010-356f-9447-33ff33fbf139 | -2.25832 | -46.76866 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca57d152-7012-3bb2-9627-5c3955a6adf8 | -2.25693 | -46.73607 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 547af6e2-a1f7-3e27-980b-5c028ecd99ec | -2.24819 | -46.77002 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7fad0fd-951e-3dda-a571-51d9efdad335 | -2.24691 | -46.71334 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 153a18ce-3895-39cb-aa42-43e47f0065d8 | -2.24487 | -46.7695 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a0fef4-085f-3cad-9e80-7282e822fb0a | -2.24082 | -46.70885 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e448cf3-8840-38fe-ba1c-6d6b895d48c0 | -2.23993 | -46.77932 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09b4391b-96de-3bd8-a32c-80e2829eabaa | -2.23878 | -46.76502 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f6e63e-3712-3640-8b19-58b0e3303f9c | -2.23823 | -46.76846 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc166953-6ede-34f6-acfa-6e779d5425ab | -2.23418 | -46.70782 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22b9c1ec-63e8-34f0-a1a0-e5d3329e11f2 | -2.23275 | -46.78173 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4463a1de-b557-335f-a119-0e867d6bf9cc | -2.23086 | -46.70731 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f74fd95d-d1da-316a-9d68-6f190678e963 | -2.20105 | -46.72385 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 132492fa-dcd8-3d48-9c37-a8cc92aac5fb | -2.19828 | -46.71989 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40c4648c-e389-3d66-ac78-988818f4d2a6 | -2.19644 | -46.49353 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f20c245-583c-3af8-80a2-e1b2266e49ca | -2.19496 | -46.71938 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 841336c0-aa5c-32a1-bb82-656a277855f6 | -2.19312 | -46.49301 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3e30373-6cef-3971-b207-3655b2a94db7 | -2.19164 | -46.71886 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a75029a-7485-3801-8c32-cf3b619e04b5 | -2.1898 | -46.49249 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a959dd9-be7f-373d-b610-07c14306d6aa | -2.18947 | -46.73264 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5412d15-266c-30a0-8559-1ba867c2e210 | -2.18778 | -46.72179 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec0b64f3-3532-386b-8ba4-5b3ad4426ecb | -2.18729 | -46.4923 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c10e471-a498-35f0-9b7f-89cef84110ea | -2.18724 | -46.72523 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9896be40-6f93-3683-b86e-ecb64570d15a | -2.18669 | -46.72868 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79130b06-f930-3035-a191-17e047f8c34b | -2.18615 | -46.73212 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f444f027-5bc1-381f-9e71-ed0287d69377 | -2.18507 | -46.73901 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c54a34-e578-3cf7-8cff-0356792dbbc3 | -2.1738 | -46.85375 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcfa3ede-c252-37c5-b72c-4d36e8a56bb3 | -2.17326 | -46.85719 | 2024-10-20 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b122f570-3169-3fb2-b478-f48800414484 | -3.90969 | -46.448 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abaef74f-63ea-3c88-a344-f37a28e4bc53 | -3.87469 | -46.4533 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ade3e89-b76a-315e-84a4-15e5499e052f | -3.83249 | -46.46106 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f903dee-dcdb-3d9b-9f20-30f1dca2ee7b | -3.83168 | -46.92265 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5413566-ee90-3b9f-bbd0-48a832c66834 | -3.83086 | -46.47148 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2aec39e0-3242-3a6e-9e03-441f871c4e73 | -3.8289 | -46.91867 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 725a9a3e-f8d1-3d3e-9d30-29ab9c1fedea | -3.82612 | -46.9147 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2f80e7c-393c-33ec-906b-00c0e56a5f5f | -3.82558 | -46.91815 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f8eb108-423b-3f58-9d4e-af5d7ed73bd8 | -3.8228 | -46.91417 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bbb3b01-0ff9-36b3-a056-477c69bb6c02 | -3.61681 | -47.51171 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dfa0dc9-4d79-3485-b8b3-e950d34fa428 | -3.61349 | -47.5112 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f53bb27d-af4e-3868-b6d2-566c43ff0094 | -3.61295 | -47.51466 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be236ce7-7131-37fc-bbaa-4df49657e2e8 | -3.61017 | -47.51068 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda45847-1fb5-32b2-8d8c-68f3a315f27e | -3.60962 | -47.51414 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17f03053-8c17-3ba2-9d7c-41e048861634 | -3.60907 | -47.5176 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90dda4f0-dab4-378d-ba27-10754cb633f1 | -3.60853 | -47.52106 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c0155ec-29ac-3f54-8bcf-5a214a2cc83a | -3.6063 | -47.51362 | 2024-10-20 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2d32ca8-8eed-362d-a7fc-8f84be5c5c8e | -3.91302 | -46.44852 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c02dbcff-b3e0-309f-b644-a1ed60d258ca | -3.86081 | -46.45467 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 813fd40e-840a-332b-b7f8-c361f9583f16 | -3.85748 | -46.45414 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96cfe0f4-6723-33b2-9cb1-b355559bd28b | -3.84257 | -46.48397 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b044db9a-9a1f-3d8d-8d80-cb553e6a5eaa | -3.83195 | -46.46454 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7de2aa6-d42a-33d0-b61f-d46eb1756c9a | -3.83141 | -46.46801 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f184de1-361f-3e73-bc7e-f766757ac59b | -3.83114 | -46.92609 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2be8a872-bcd4-3701-891b-b288443cee36 | -3.82836 | -46.92213 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4b6607-ac05-3eec-84fd-dd6655af88e0 | -3.82226 | -46.91763 | 2024-10-20 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cb44890-a77a-35db-8dbf-76d33c660bf5 | -3.77826 | -46.65911 | 2024-10-20 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
